from datetime import *
from random import *
k=0
while True:
    k+=1
    a=randint(1,50)
    b=randint(1,50)
    p=0
    while p!=3:
        p+=1
        v=int(input("Millega võrdub {0}+{1}= ".format(a,b)))
        if v==a+b:
            print("Tubli!")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(a,b,a+b))
    if k==5:break

total_attempts = 5
correct_answers = 0

print("Добро пожаловать в игру сложения!")
print("Вы должны угадать результат сложения двух случайных чисел от 1 до 50.")

for attempt in range(1, total_attempts + 1):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct_sum = num1 + num2

    user_answer = int(input(f"Сколько будет {num1} + {num2}? Ваш ответ: "))

    if user_answer == correct_sum:
        correct_answers += 1
        print("Правильно! Молодец!")
    else:
        print(f"Неправильно. Правильный ответ: {correct_sum}")

print(f"\nИгра завершена. Вы правильно ответили на {correct_answers} из {total_attempts} вопросов.")


















#from datetime import *
#from random import *


#summa=0
#for i in range(10):
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#print(summa)
#summa=0
#i=0
#while True:
#    i+=1
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#    if i==10: break
#print(summa)







##sum_arvud = 0
##while True:
#    try:
#        input_str = input("Sisestage arv (või vajutage lõpetamiseks Enter): ")
#        if not input_str:
#            break  # Прерываем цикл, если введенная строка пуста (Enter)
#        number = float(input_str)
#        sum_arvud += number
#    except ValueError:
#        print("Viga! Sisestage õige numbe.")





#1
#from random import *
#from datetime import *
#nimi=input("Mis on sinu nimi?").capitalize
#mitu=int(input("Mitu korda tervitada?"))
#for i in range(1,mitu+1):
#    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")





#Таблица умножения на 5
#from random import *
#from datetime import *

#korrutamine=["5"]
#arv=["1","2","3","4","5","6","7","8","9","10"]
#for i in range(10):
#   tulemus = int(arv[i]) * 5
#   print(f"{arv[i]} * 5 = {tulemus}")







#from random import *
#from datetime import *
##komm
#print("1. variandt -while True-")
#while True:
#    v=input("Tahan komme!").lower()
#    if v=="komm": break


#print("2. variandint -while tingimusega-")
#v=""
#while v!="komm":
#     v=input("Tahan komme!").lower()







##from random import *
##from datetime import *

#paevad=["Esmapäev","Tesipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
#tunnid=["8 tundi","9 tundi","2 tundi","7 tundi","4 tundi","tuni pole","tundi pole"] 
#for i in range(7):
    #print(paevad[i]+"-"+tunnid[i])








#from random import *
#from datetime import *
#arve_nr=datetime.now() #date.today()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#tooded=["Piim","Leib","Komm"] #index 0-1-2
#for i in range(3): #Первое число равно 3 второе число равно 2 и третье число равно 1
#    toode="piim"[i]
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
#    if v=="jah":
#       mitu=int(input("Mitu?"))
#       tsekk+=toode+ " "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#       summa+mitu*hind


#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)