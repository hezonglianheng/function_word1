# encoding: utf8
import csv
from tkinter import filedialog
import re
import logging
import utils
from matplotlib import pyplot as plt
from matplotlib import font_manager as fmg


def origin_analysis(word, condition):
    if word == '更加':
        origin_path = r'./corpus/更加.txt'
        changed_path = r'./results/越发2022-10-04.csv'
    elif word == '越发':
        origin_path = r'./corpus/越发.txt'
        changed_path = r'./results/更加2022-10-05.csv'
    else:
        logging.info(
            '输入的词语：{}错误，请重试！'.format(word)
        )
        return

    with open(origin_path, 'r') as origin:
        origin_lines = origin.readlines()
    with open(changed_path, 'r', newline='') as changed:
        changed_reader = csv.reader(changed)

        idx = -1
        origin_count = 0
        condition_count = 0
        for record in changed_reader:
            idx += 1
            if record[1] == '0' or record[1] == '1' \
                    or record[1] == '2':
                origin_count += 1
                if re.search(condition, origin_lines[idx]):
                    condition_count += 1

        logging.info(
            '共有{}个句子，在“{}”下，得到句子{}句，占比{}'.
            format(origin_count, condition, condition_count,
                   condition_count / origin_count)
        )


def changed_analysis(word, condition):
    if word == '更加':
        changed_path = r'./results/更加2022-10-05.csv'
    elif word == '越发':
        changed_path = r'./results/越发2022-10-04.csv'
    else:
        return

    with open(changed_path, 'r',
              newline='') as changed:
        changed_reader = csv.reader(changed)

        changed_counts = [0, 0, 0]
        sum_of_changed = 0
        labels = ['0类句', '1类句', '2类句']
        for r in changed_reader:
            sum_of_changed += 1
            if re.search(condition, r[0]):
                if r[1] == '0':
                    changed_counts[0] += 1
                elif r[1] == '1':
                    changed_counts[1] += 1
                elif r[1] == '2':
                    changed_counts[2] += 1

    font = fmg.FontProperties(fname='./config/simsun.ttc')
    patches, texts, autotexts = plt.pie(
        x=changed_counts, labels=labels,
        autopct='%.2f%%', shadow=True
    )
    plt.title(
        label='“{}”句子集中3类句匹配“{}”的情况'.
        format(word, condition),
        fontdict={
            'font': font,
            'size': 16
        }
    )
    for i in range(len(autotexts)):
        texts[i].set(fontproperties=font,
                     fontsize=16)
        autotexts[i].set(fontproperties=font,
                         fontsize=16)
    logging.info(
        '共有句子{}句，符合条件的句子{}句，占比{}'.format(
            sum_of_changed, sum(changed_counts),
            sum(changed_counts) / sum_of_changed
        )
    )
    plt.show()


def main():
    log_file = filedialog.askopenfilename(
        initialdir=r'./log_file',
        title='指定日志文件'
    )
    utils.get_logger(log_file)
    word = input('考察词：')
    logging.info(
        '本次考察的词语是：{}'.format(word)
    )
    condition = input(
        '待匹配的正则表达式：'
    )
    is_origin = input(
        '是否为原始文件？[y/n]'
    )
    if is_origin == 'y':
        origin_analysis(word, condition)
    elif is_origin == 'n':
        changed_analysis(word, condition)


if __name__ == '__main__':
    main()
