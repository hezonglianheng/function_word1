# encoding: utf8
import csv
from datetime import date
import logging
from tkinter import filedialog
import utils


def main():
    log_file = filedialog.askopenfilename(
        initialdir='./log_file',
        title='选择日志文件'
    )
    utils.get_logger(log_file)
    origin_file = filedialog.askopenfilename(
        initialdir=r'./corpus',
        title='选择标注文件'
    )
    logging.info(
        '标注文件为{}'.format(origin_file)
    )
    word = input('请输入标注词：')
    logging.info(
        '标注词为{}'.format(word)
    )
    use_new = input('是否使用新文件？[y/n]')
    if use_new == 'y':
        result_file = r'./results/' + 'task3' + word + \
                      str(date.today()) + '.csv'
        f = open(result_file, 'w')
        f.close()
    elif use_new == 'n':
        result_file = filedialog.askopenfilename(
            initialdir='./results',
            title='选择结果存放文件'
        )
    else:
        return
    logging.info(
        '结果存放于{}'.format(result_file)
    )

    with open(origin_file, 'r') as f:
        corpus = f.readlines()

    with open(result_file, 'a', newline='') as f:
        writer = csv.writer(f)

        for i in range(len(corpus)):
            print(corpus[i])
            judge = input(
                '句中是否明确指出时间（0无，1有，x不适用，q退出）？'
            )
            if judge == 'q':
                file_name = './corpus/task3暂存'+word+'.txt'
                with open(file_name, 'w') as z:
                    z.writelines(corpus[i:])
                logging.info(
                    '本次标注了{}条文本'.format(i)
                )
                return None
            else:
                writer.writerow(
                    [
                        corpus[i], judge
                    ]
                )


if __name__ == '__main__':
    main()