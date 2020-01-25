def file_wr():
    str1 = '1'
    f = open('ex01.txt', 'w')
    while str1:
        str1 = input('Input string ')
        f.writelines(str1)
        f.writelines('\n')
    f.close()

file_wr()