# encoding: utf8
import random
from tkinter import filedialog


def main():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        lines = f.readlines()

    while True:
        is_check = input('是否检查[y/n]？')
        if is_check == 'n':
            break
        elif is_check == 'y':
            idx = random.randint(0, len(lines)-1)
            print(lines[idx])


if __name__ == '__main__':
    main()