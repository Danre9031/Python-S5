# ; 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# ; Модуль сжатия:
# ; Для чисел:
# ; Входные данные:
# ; 111112222334445
# ; Выходные данные:
# ; 5142233415
# ; Также должно работать и для букв:
# ; Входные данные:
# ; AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# ; Выходные данные:
# ; 6A1F2D7C1A17E
# ; (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# ; Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def rle_encode(incoded):
    codedString=""
    count=0
    firstCoded= incoded[0]
    for coded in incoded:
        if not coded == firstCoded:
            codedString+=f"{count}{firstCoded}"
            firstCoded=coded
            count=1
        else:
            count+=1
    else:
        codedString+=f'{count}{firstCoded}'
    return codedString


def rle_decode(incoded):
    coded_string=""
    swith=True
    for coded in incoded:
        if swith==True:
            count= int(coded)
            swith = False
        else:
            coded_string+=count*coded
            swith = True

    return coded_string
command=int(input("введите что хоти сделать закодировать(1) декодировать (2): "))
if command==1:
    incoded=input("Введите код для кодировки :")
    print(rle_encode(incoded))
elif command==2:
    incoded=input("Введите код для декодировки (в кодированом коде количесвто закодированых елементов должно не превышать 9шт) :")
    print(rle_decode(incoded))


