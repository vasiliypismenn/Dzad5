#40. Реализуйте RLE алгоритм:
#  реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел: Входные данные: 111112222334445
# Выходные данные:           5142233415
# Также должно работать и для букв:
# Входные данные:  AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные: 6A1F2D7C1A17E

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для сжатия: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
