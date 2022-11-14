# coding:utf-8
import re
import os
from cloud import *

"""
中文分句
"""


def normal_cut_sentence(text):
    text = re.sub(r'([。！？])([^’”]?)', r'\g<1>\n\g<2>', text)  # ？。！
    text = re.sub(r'(…{2})([^’”])', r'\g<1>\n\g<2>', text)  # ……
    text = re.sub(r'(.{6})([^’”])', r'\g<1>\n\g<2>', text)  # ......
    text = re.sub(r'([。！？…{2}][’”])([^’”])', r'\1\n\2', text)  # “”
    return text.split("\n")


def cut_sentence_with_quotation_marks(text=''):
    """
    具体思路: 针对中文进行分句, 在中文里面其实存在言语和非言语部分,
    言语主要指的是: “这是一个 python 程序”, 他说……
    非言语就是一个普通的句子
    至于说话的句子内部需不需要进行二次分句这个需要去定义
    列举当前可能出现的一些情况
    1. “这是一段文本！应该保留的” -> “这是一段文本！应该保留的”
    2. 这是一段文本！应该保留的。-> 这是一段文本！，应该保留的
    对于话语类型的, 是否需要把话语与前后xxx说连在一起?
    """

    # p = re.compile(r'(“.*?”)|(.*?[。！？…]{1,2}”)|(.*?[。！？…]{1,2}”?)')
    p = re.compile(r'(“.*?”)|(.*?[。！？…]{1,2}”?)')
    text = text.replace('\n', '')
    list = []
    # for i in p.finditer(text):
    #     print(i)
    # return []
    for i in p.finditer(text):
        temp = ''
        start = i.start()
        end = i.end()
        for k in range(start, end):
            temp += text[k]
        if temp != '':
            list.append(temp)
    return list


if __name__ == '__main__':
    """
    基于输入路径在example中拼接读取路径
    path = input('请输入文件路径:')
    """
    curr_path = os.path.dirname(__file__)
    path = os.path.abspath(curr_path + r'/example/content.txt')
    with open(path, 'r', encoding="utf-8") as f:
        text = f.read()
    result = cut_sentence_with_quotation_marks(text)

    """
    new_data = re.findall('[\u4e00-\u9fa5]+', result[0], re.S)
    new_data = "".join(new_data)
    seg_list_exact = jieba.cut(new_data)
    print('new_data', seg_list_exact)
    for i in seg_list_exact:
        print(i)
    exit(0)
    """

    word_lists = []
    for index, item in enumerate(result):
        result = cut_word(item)
        for i in result:
            word_lists.append(i)
    print(word_lists)
    render_cloud(word_lists)
