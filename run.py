from tkinter import filedialog
from utils import get_logger
import logging
import os.path
import mark


def main():
    log_file = filedialog.askopenfilename(
        initialdir=r'./log_file',
        title='选择日志文件'
    )
    get_logger(log_file)
    corpus_file = filedialog.askopenfilename(
        initialdir=r'./corpus',
        title='选择待标注文件'
    )
    logging.info(
        '标注文件为：{}'.format(
            os.path.abspath(corpus_file)
        )
    )
    result_file = filedialog.askopenfilename(
        initialdir=r'./results',
        title='选择结果存放文件'
    )
    logging.info(
        '结果将存放在：{}'.format(
            os.path.abspath(result_file)
        )
    )
    mark.main(corpus_file, result_file)


if __name__ == '__main__':
    main()