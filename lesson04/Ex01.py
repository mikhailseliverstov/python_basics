from sys import argv
name, param1, param2, param3 = argv

zp = int(param1)*int(param2) + int(param3)

print(f'Заработная плата = {zp}')