def program1488():
    # import math
    # №1.1 Точные квадраты
    # N = int(input())
    # i = 1
    # while i*i <= N:
    #     print(i*i)
    #     i += 1
    
    # №1.2 слово - буква
    # a = input()
    # print(a)
    # while len(a) >= 2:
    #     a = a[1:-1]
    #     print(a)
    
    # №1.3 Спортсмен
    # x, y = map(int, input().split())
    # n = 1
    # while x < y:
    #     x *= 1.15
    #     n += 1
    # print(n)
    
    # №1.4 Вася и носки
    # n, m = map(int, input().split())
    # day = 0
    # while n > 0:
    #     day += 1
    #     n -= 1
    #     if day % m == 0:
    #         n += 1
    # print(day)
    
    # №1.5 Миша и Боба
    # a, b = map(int, input().split())
    # years = 0
    # while a <= b:
    #     a *= 3
    #     b *= 2
    #     years +=1
    # print(years)
    
    # №1.6 ВВод чисел 0
    # a = int(input())
    # while a != 0:
    #     a = int(input())
    
    # №1.7 Архетиктура компьютера
    # a = int(input())
    # i = 0
    # while 2**i < a:
    #     i += 1
    # if 2 ** i == a:
    #     print(i)
    # else:
    #     print('Нет')
    
    # №1.8 Зимний вечер в Бурсе
    # a = int(input())
    # while a < 1000000000 and str(a)[0] != '1':
    #     a *= int(str(a)[0])
    # print(a)
    
    # №1.9 Бал в БерлГУ
    # n = int(input())
    # a = list(map(int, input().split()))
    # m = int(input())
    # b = list(map(int, input().split()))
    # a.sort()
    # b.sort()
    # count = 0
    # i = 0
    # j = 0
    # while i < n and j < m:
    #     if abs(a[i] - b[j]) <= 1:
    #         count += 1
    #         i += 1
    #         j += 1
    #     elif a[i] - b[j] > 1:
    #         j += 1
    #     elif b[j] - a[i] > 1:
    #         i += 1
    # print(count)
    
    # №1.10 Ваня и кубики
    # n = int(input())
    # i = 0
    # j = 0
    # count =0
    # while n > 0:
    #     j += 1
    #     i += + j
    #     n -= i
    #     if n >= 0:
    #         count +=1
    # print(count)
    
    # №1.11 Система уравнений
    # n, m = map(int, input().split())
    # a = 0
    # b = 0
    # count = 0
    # # a = m - b ** 2
    # # b = n - (m - b ** 2) ** 2
    # while b <= n:
    #     if b == n - (m - b ** 2) ** 2:
    #         a = m - b ** 2
    #         if a >= 0:
    #             if a ** 2 + b == n and a + b ** 2 == m:
    #                 count += 1
    #     b += 1
    # print(count)
    
    # №1.12 Новогодние свечки
    # a, b = map(int, input().split())
    # c = 0
    # day = 0
    # while a > 0:
    #     a -= 1
    #     day += 1
    #     c += 1
    #     if c == b:
    #         a += 1
    #         c = 0
    # print(day)
    
    # №1.13 Новый год и спешка
    # n, k = map(int, input().split())
    # i = 0
    # while k + 5 * (i + 1) <= 240 and i < n:
    #     i += 1
    #     k += 5 * i
    # print(i)
    
    # №1.14 Дело о нулях и единицах
    # n = int(input())
    # s = input()
    # i = 0
    # while i < n-1:
    #     if s.count('0') == 0:
    #         i = n
    #     elif s.count('1') == 0:
    #         i = n
    #     elif s[i] != s[i+1]:
    #         s = s.replace('0', '', 1)
    #         s = s.replace('1', '', 1)
    #         n -= 2
    #         i = -1
    #     i += 1
    # print(len(s))
    
    # n = int(input())
    # s = input()
    # while '01' in s or '10' in s:
    #     s = s.replace('10', '')
    #     s = s.replace('01', '')
    # print(len(s))
    
    # n = int(input())
    # s = input()
    # print(abs(s.count('1')-s.count('0')))
    
    # ОБХОД ВСЕХ ЦИФР ЧИСЛА С ПОМОЩЬЮ WHILE
    # x = int(input())
    # diff = 0
    # diff_chet = 0
    # summ = 0
    # proiz = 1
    # maximum = 0
    # minimum = 9
    # while x > 0:
    #     last = x % 10
    #     diff += 1
    #     if last % 2 == 0:
    #         diff_chet += 1
    #     summ += last
    #     proiz *= last
    #     if last > maximum:
    #         maximum = last
    #     if last < minimum:
    #         minimum = last
    #     x = x // 10
    # print('Колличество цифр', diff)
    # print('Сумма цифр', summ)
    # print('Колличество четных цифр', diff_chet)
    # print('Произведение', proiz)
    # print('Самая большая цифра', maximum)
    # print('Самая маленькая цифра', minimum)
    
    # x = int(input())
    # while x > 0:
    #     last = x % 2
    #     print(last)
    #     x = x // 2
    
    
    # №2.1 Жизнь без нулей
    a = int(input())
    b = int(input())
    c = a + b
    ad = int(str(a).replace('0', ''))
    bd = int(str(b).replace('0', ''))
    cd = int(str(c).replace('0', ''))
    if ad + bd == cd:
        print('YES')
    else:
        print("NO")
    # print('a = ', a)
    # print('b = ', b)
    # print('c = ', c)
    # print('ad = ', ad)
    # print('bd = ', bd)
    # print('cd = ', cd)