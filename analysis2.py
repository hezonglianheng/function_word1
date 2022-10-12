# encoding: utf8
import csv
from tkinter import filedialog
import logging
import utils
from matplotlib import pyplot as plt
from matplotlib import font_manager as fmg


def main():
    log_file = filedialog.askopenfilename(
        initialdir='./log_file',
        title='选择日志文件'
    )
    utils.get_logger(log_file)
    word = input('请输入分析词：')
    if word == '越发':
        path = './results/越发2022-10-12.csv'
    elif word == '更加':
        path = './results/更加2022-10-11.csv'
    else:
        return None

    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)

        counts = [0, 0, 0, 0]
        labels = ['verb', 'adjective', 'noun', 'others']
        for item in reader:
            if item[1] == 'v':
                counts[0] += 1
            elif item[1] == 'a':
                counts[1] += 1
            elif item[1] == 'n':
                counts[2] += 1
            elif item[1] == 'o':
                counts[3] += 1

        font = fmg.FontProperties(fname='./config/simsun.ttc')
        patches, texts, autotexts = plt.pie(
            x=counts, labels=labels, autopct='%.2f%%',
            shadow=True
        )
        plt.title(
            label='{}修饰各词类的情况'.format(word),
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
            '共有句子{}句'.format(sum(counts))
        )
        plt.show()


if __name__ == '__main__':
    main()