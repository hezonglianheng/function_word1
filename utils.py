# encoding: utf8
import logging


def get_logger(file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    s_handler = logging.StreamHandler()
    s_formatter = logging.Formatter(
        '{asctime}: {levelname}: {message}', style='{'
    )
    s_handler.setFormatter(s_formatter)
    f_handler = logging.FileHandler(file)
    f_formatter = logging.Formatter(
        '{asctime}: {levelname}: {message}', style='{'
    )
    f_handler.setFormatter(f_formatter)
    logger.addHandler(s_handler)
    logger.addHandler(f_handler)
