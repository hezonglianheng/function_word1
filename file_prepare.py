import re


def main():
    with open('./corpus/更加原始.txt', 'r') as f:
        origin_gengjia = f.readlines()

    new_gengjia = []
    for item in origin_gengjia:
        new_gengjia.append(item.replace('[加]', '加'))

    with open('./corpus/越发原始.txt', 'r') as f:
        origin_yuefa = f.readlines()

    new_yuefa = []
    for item in origin_yuefa:
        new_yuefa.append(item.replace('[发]', '发'))

    final_gengjia = []
    final_yuefa = []
    replaced_gengjia = []
    replaced_yuefa = []
    for item in new_gengjia:
        if re.search('更加', item):
            final_gengjia.append(item)
            replaced_yuefa.append(
                item.replace('更加', '越发')
            )
    for item in new_yuefa:
        if re.search('越发', item):
            final_yuefa.append(item)
            replaced_gengjia.append(
                item.replace('越发', '更加')
            )

    with open('./corpus/越发.txt', 'w') as f:
        f.writelines(final_yuefa)
    with open('./corpus/更加.txt', 'w') as f:
        f.writelines(final_gengjia)
    with open('./corpus/r_越发.txt', 'w') as f:
        f.writelines(replaced_yuefa)
    with open('./corpus/r_更加.txt', 'w') as f:
        f.writelines(replaced_gengjia)


if __name__ == '__main__':
    main()