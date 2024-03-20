from pprint import pprint
import datetime

f = open('songs.csv', encoding='utf8').readlines()
print(f[0])
f = f[1:]

arr = [[x for x in i.rstrip('\n').split(';')] for i in f]


# Задание 1
def the_first(arr: list) -> list:
    """
    
    Описание аргументов:
    : `arr` - массив с песнями

    """
    for x in arr: x[-1] = x[-1].split('.')
    
    new_arr = []
    for x in arr:
        date = x[-1]

        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

        if year<=2002: # не позже 2002
            if year==2002: # не позже второго месяца
                # if int(date[2])== 1:
                #     if int(date[1])<= 1:
                if month==1:
                    if day<=1:
                        new_arr.append(x)
            elif year<2002:
                new_arr.append(x)


    for i in range(len(new_arr)):
        x = new_arr[i]

        if x[0] == 'unknown':
            date = x[-1]

            day = int(date[0])
            month = int(date[1])
            year = int(date[2])


            L_n = len(x[1])
            L_s = len(x[2])
            data_delta = (datetime.date(2002, 1, 1) - datetime.date(year, month, day)).days

            t_n = abs( (data_delta)/(L_n + L_s) ) * 10_000
            
            x[0] = str(t_n)

    for x in new_arr: x[-1] = '.'.join(x[-1])

    open('songs_new.csv', 'w')
    with open('songs_new.csv','a', encoding='utf8') as f:
        for i in new_arr:
            f.write(';'.join(i)+'\n')
            print(f"{i[2]} - {i[1]} - {i[0]}")

        
    return new_arr

# Задание 2
def quickSort(array: list) -> list:
    """
        Функция быстрой сортировки 

        : `array` - массив данных
    """
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []

        for item in array:
            
            day = int(item[-1].split('.')[0])
            month = int(item[-1].split('.')[1])
            year = int(item[-1].split('.')[2])


            day_piv = int(pivot[-1].split('.')[0])
            month_piv = int(pivot[-1].split('.')[1])
            year_piv = int(pivot[-1].split('.')[2])


            if datetime.date(year, month, day) == datetime.date(year_piv, month_piv, day_piv):
                equal_lst.append(item)
            elif datetime.date(year, month, day) > datetime.date(year_piv, month_piv, day_piv):
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return array


def the_second(arr: list) -> list:
    """
    
    : `arr` - Массив с песнями
    
    """
    cntr = 1
    for i in quickSort(arr)[:5]:

        print(cntr, i[2], i[-1])
        cntr+=1


# Задание 3
def the_third(arr: list) -> bool:
    """
    
    : `arr` - Массив с песнями
    
    """    
    x = input('Введите название: ')
    while x != '0':

        for i in arr:
            if i[2] == x:
                print(f'У {i[1]} найдена песня: {i[2]}')

        x = input('Введите название: ')


# Задание 4
def the_fourth():

    russian_artists = []
    foreign_artists = []

    f_ru = [i.rstrip('\n') for i in open('russian_artists.txt', encoding='utf8').readlines()]
    f_en = [i.rstrip('\n') for i in open('foreign_artists.txt', encoding='utf8').readlines()]

    f_gen = f_ru+f_en
    print(f_gen)

    dic = 'йцукенгшщзхэждлорпавыфячсмитьбюё'

    for name in f_gen:
        for x in name.lower():
            if x in dic:
                russian_artists.append(name)
                break
        else:
            foreign_artists.append(name)
    
    russian_artists = set(russian_artists)
    foreign_artists = set(foreign_artists)

    print(f'Количество российских исполнителей: {len(russian_artists)}')
    print(f'Количество иностранных исполнителей: {len(foreign_artists)}')


    open('russian_artists.txt', 'w', encoding='utf8').write('\n'.join(russian_artists))
    open('foreign_artists.txt', 'w', encoding='utf8').write('\n'.join(foreign_artists))
    

the_fourth()