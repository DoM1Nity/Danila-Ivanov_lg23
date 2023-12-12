from random import *
from math import *

try:
    P=int(input("Sõbrade kogus: "))
except :
    print("Kogus on täisarv")
hind=12.90
hind*=hind*1.1 #hind+10%
print("Igaüks maksb ", hind/P)







#9

#from random import *
#from math import *

#try:
#    a=int(input("a: "))
#except :
#    print("On vaja taäsarv kasutada!")
#try:
#     b=int(input("b: "))
#except :
#    print("Viga muutujaga!")
#try:
#     c=int(input("c: "))
#except :
#     print("Viga muutujaga!")

#P=a+b+c 
#print("Perimetr/Ümbermõõt: "P)

#print("@..@".center(10," ")) #center сам распрделяет текст по середине учитывая заданое число ему 
#print("(----)".center(10," "))
#print("( \__/ )".center(10," "))
#print("^^ "" ^^".center(10," "))   #жаба






#from random import *
#from math import *
#try:
#    min_=int(input("Min: "))
#except :
#    print("On vaja täisarv kasutada!")
#try:
#    max_=int(input("Max: "))
#except :
#    print("Viga max_ muutujuga")


#a1=randint(min_,max_)
#a2=randint(min_,max_) 
#a3=randint(min_,max_) 
#a4=randint(min_,max_) 
#a5=randint(min_,max_) 
#keskmine=(a1+a2+a3+a4+a5)/5 #Деление всех чисел на 5 
#print("Arvud: {0},{1},{2},{3},{4}. Aritmetiline keskmine on: {5}".format(a1,a2,a3,a4,a5,keskmine)) #подсчет остальных чисел для вычисления среднеарифмитечского








##На сегодняшнем уроке мы будем делать проверку, и исправлять ошибки 12.12.2023
#6
#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? ")) ##попытка ввести значения времени
#    try: #помогает избежать ошибки при вводе букв а не цифр(try,expect)try:
#        teepikkus = float(input("Mitu kilomeetrit sõitsid? ")) #попытка ввести значения расстояния
#        kiirus = aeg / teepikkus #рассчет скорости
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    except :
#        print("Viga andmetaga")
#except :
#    print("On vaja ainult numbrid sisesta!")











#5
#from math import *

#a=float(input("pikkus:"))
#b=float(input("ladius:"))
#d=sqrt(a**2+b**2)
#print("Diagonaal=",d,"m") 


#from random import *
#from math import *
#from xml.etree.ElementTree import PI

#u=float(input("Ümbermõõt")) #L=pi*2*r=pi*d
#d=round(u/pi,2) 
#print("Läbimõõt =" ,d)






#4

#from random import *
#kokku=randint(1,100)
#print("Laual peal on", kokku, "kommid. Mitu tahad süüa")
#kommid=int(input())
#kokku-=kommid
#print("Nüüd kokku on",kokku)



#3

#vanus=18
#eesnimi="Jaak"
#pikkus=16.5
#kas_käib_koolis=True

#print("Muutuja vanus=",vanus,"on", type (vanus))
#print("Muutuja eesnimi=",eesnimi,"on", type (eesnimi))
#print("Muutuja pikkus=",pikkus,"on", type (pikkus))
#print("Muutuja kas_käib_koolis=",kas_käib_koolis,"on", type (kas_käib_koolis))



#2

#arv=float(input("Arv1: "))
#t=input("Tehe: ")
#arv=float(input("Arv2: "))
#vastus=eval(str(arv1)+t+str(arv2))
#print(str(arv1)+t+str(arv2)+"="+str(vastus))
#print(arv1,t,arv2,"=",vastus,sep="")        #разделитель
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastlus))


#-------------------------------------------------------------------
#1

#print ("Tere maailm!".center(75,"-"))
#nimi=input("Mis on sinu nimi? ").capitalize() #python->Python
#print("Tere "+nimi+"!")
#print("Tere",nimi+"!")
#print("Tere {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled"))           #"21"! не ровно=21
#print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja nimi=", nimi, type(nimi))
#print("Muutuja vanus=",vanus,type(vanus))
