# encoding: utf8
import matplotlib.pyplot as plt
import csv
from tkinter import filedialog
import matplotlib.font_manager as fmg


def draw_pie_chart_of_sentence_type():
    draw_from = filedialog.askopenfilename(
        initialdir='./results',
        title='选择绘图所需文件'
    )
    chart_title = input('绘制饼图标题：')
    font = fmg.FontProperties(fname='./config/simsun.ttc')
    with open(draw_from, 'r',
              encoding='gbk',
              newline='') as f:
        reader = csv.reader(f)
        nums = [0, 0, 0]
        labels = [u'1类句', u'2类句', u'0类句']
        for item in reader:
            if item[-1] == '0':
                nums[2] += 1
            elif item[-1] == '1':
                nums[0] += 1
            elif item[-1] == '2':
                nums[1] += 1

        valid_s = sum(nums)

        patches, texts, autotexts = plt.pie(
            x=nums, labels=labels, autopct='%.2f%%',
            shadow=True,
        )
        plt.title(chart_title,
                  fontdict={
                      'font': font,
                      'size': 16
                  })
        plt.text(0.8, -1.25,
                 '有效句共计{}句'.format(valid_s),
                 fontdict={
                     'font': font,
                     'size': 16
                 })
        for i in range(len(autotexts)):
            texts[i].set(fontproperties=font,
                         fontsize=16)
            autotexts[i].set(fontproperties=font,
                             fontsize=16)

        plt.show()


if __name__ == '__main__':
    draw_pie_chart_of_sentence_type()