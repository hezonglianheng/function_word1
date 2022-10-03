import csv
from datetime import date


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
                '合法性判定（0，非法；1，合法；q，退出标注）：'
            )
            if legal == '0' or legal == '1':
                result_writer.writerow(
                    [corpus[i], legal]
                )
            elif legal == 'q':
                word = input('标注词：')
                now = str(date.today())
                file_name = './corpus/' + word + now + '.txt'
                with open(file_name,
                          mode='w',
                          encoding='gbk') as f:
                    f.writelines(corpus[i:])
                return None
