import jieba
import collections
import re
from wordcloud import WordCloud
import os


def cut_word(sentence):
    valid = re.compile(r'[\u4e00-\u9fa5]+')
    sentence = valid.findall(sentence, re.S)
    sentence = " ".join(sentence)
    seg_list_exact = jieba.lcut(sentence)
    final_list = remove_stop_word(seg_list_exact)
    return final_list


def remove_stop_word(seg_list_exact):
    """
    移除分词结果中的频用词
    """
    curr_path = os.path.dirname(__file__)
    result_list = []
    stop_word_path = os.path.abspath(curr_path + '/resources/stop_words.txt')
    with open(stop_word_path, 'r', encoding='utf-8') as f:
        con = f.readlines()
        stop_words = set()

    for i in con:
        stop_words.add(i.replace('\n', ''))

    for word in seg_list_exact:
        if word not in stop_words and len(word):
            result_list.append(word)

    return result_list


def render_cloud(word_count):
    word_count = " ".join(word_count)
    font_path = r'C:\Windows\Fonts\simfang.ttf'

    wc = WordCloud(
        width=200,
        height=150,
        background_color='white',
        max_font_size=100,
        min_font_size=10,
        scale=2,
        font_path=font_path
    )
    wc.generate(word_count)

    curr_path = os.path.dirname(__file__)
    wc.to_file(curr_path + './cloud.jpg')
