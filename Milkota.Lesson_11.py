#ДЗ
#Если функция принимает от нас кортеж-считаем длинну кортежа.
#Если список:количество строк и чисел
#Если число:количество нечетных цифр
#Если строку:количество гласных
#

def fn(A):
    if type(A)==tuple:
        print('Длинна заданного кортежа: ',len(tup))
    elif type(A)==list:
        kol_s=0
        kol_i=0
        for i in lis:
            if type(i)==str:
                kol_s+=1
            elif type(i)==int:
                kol_i+=1
        print('Количество строк в заданном списке: ',kol_s,'\n','Количество чисел в заданном списке: ',kol_i)
    elif type(A)==int:
        nech=0
        for i in str(A):
            if int(i)%2!=0:
                nech+=1
        print('Нечетных цифр в заданном числе: ',nech)
    elif type(A)==str:
        vowels=0
        for i in A:
            if i in 'aeuioёуыяаеиоюэ':
                vowels+=1
        print('Количество гласных в заданной строке: ',vowels)

tup=(4,99,'rtf',45,'edhu')
lis=[88,34,'ryu','svyi',79,2]
x=429973
st='c7ijds0gsezйыалдо678'

fn(tup)
fn(lis)
fn(x)
fn(st)
