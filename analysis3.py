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
    word = input(
        '分析词：'
    )
    logging.info(
        '本次分析词为：{}'.format(word)
    )
    analysis_file = filedialog.askopenfilename(
        initialdir='./results',
        title='选择分析文件'
    )
    logging.info(
        '本次分析的文件为：{}'.format(analysis_file)
    )

    with open(analysis_file, 'r', newline='') as file:
        reader = csv.reader(file)

        counts = [0, 0]
        labels = ['无时间性', '有时间性']
        for item in reader:
            if item[1] == '0':
                counts[0] += 1
            elif item[1] == '1':
                counts[1] += 1

        font = fmg.FontProperties(fname='./config/simsun.ttc')
        patches, texts, autotexts = plt.pie(
            x=counts, labels=labels, autopct='%.2f%%',
            shadow=True
        )
        plt.title(
            label='“{}”时间性的考察情况'.format(word),
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
