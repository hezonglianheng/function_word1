import csv
from datetime import date
import logging


def main(corpus_file, result_file):
    with open(
        corpus_file, mode='r',
        encoding='gbk'
    ) as file:
        corpus = file.readlines()

    with open(
        result_file, mode='a',
        encoding='gbk',
        newline=''
    ) as result:
        result_writer = csv.writer(result)
        for i in range(len(corpus)):
            print(corpus[i])
            legal = input(
                '合法性判定（0，非法；1，合法；2，不确定；x，不适用；q，退出标注）：'
            )
            if legal == 'q':
                word = input('标注词：')
                now = str(date.today())
                file_name = './corpus/' + word + now + '.txt'
                with open(file_name,
                          mode='w',
                          encoding='gbk') as f:
                    f.writelines(corpus[i:])
                logging.info('本次标注了{}条文本。'.format(i))
                return None
            else:
                result_writer.writerow(
                    [corpus[i], legal]
                )

    logging.info('标注完成！')
