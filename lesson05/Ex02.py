def file_count():
    str_cnt = 0
    with open('Ex02.txt') as f:
        for num, st in enumerate(f):
            str_cnt += 1
            print(f'Length of string {num+1} = {len(st)}')
    print(f'There is {str_cnt} strings in file')

file_count()