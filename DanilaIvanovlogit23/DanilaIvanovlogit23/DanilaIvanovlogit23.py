#8
from random import *
from datetime import *
arve_nr=datetime.now() #date.today()
print(arve_nr)
import datetime

x = datetime.datetime.now()

tsekk="Arve: 12345\nToode Hind Kogus Summa"
summa=0
toode="piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
  mitu=int(input("Mitu?"))
  tsekk+=toode+" "+str(hind)+" "+str(mitu)+ " "+str(mitu*hind)+ "\n"
  summa+=mitu*hind
toode="leib"
hind=randint(50,150)/100
v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
  mitu=int(input("Mitu?"))
  tsekk+=toode+" "+str(hind)+" "+str(mitu)+ " "+str(mitu*hind)+ "\n"
  summa+=mitu*hind
toode="saia"
hind=randint(50,150)/100
v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
  mitu=int(input("Mitu?"))
  tsekk+=toode+" "+str(hind)+" "+str(mitu)+ " "+str(mitu*hind)+ "\n"
  summa+=mitu*hind
  tsekk+="Kokku maksta: "+str(summa)





#7
#sugu=input("Kas sa oled mees või naine").lower()
#if sugu=="naine" or sugu=="n" :
#    l1=135
#    l2=180
#    l3=200
#elif  sugu=="mees" or sugu=="m" :
#    l1=150
#    l2=165
#    l3=180
#else:
#    l1=0
#    print("Viga")
#    if l1!=0:
#try:
#    pikkus=int(input("Sisesta oma pikkus: "))
#    if pikkus>29 and pikkus<l1:
#      vastus="luhike"
#    elif pikkus>=l1 and pikkus>l2:
#      vastus="keskmine"
#    elif pikkus>l2 and pikkus<=l3:
#      vastus="pikk" 
#    else:
#         vastus="tundmatu"
#    print("Sinu pikkus on {0}".format(vastus))
#except :
#    print("Неправильный формат")





##6

#try:
#    hight=int(input("Какого ты роста?"))
#    if hight>0 and hight<100:
#      print ("Ты низкого роста")
#    elif 80 < hight <= 135 :
#      print ("Ты среднего роста")
#    elif 165 < hight <= 180 :
#      print ("Ты высокого роста")
#    elif 180 < hight <= 200 :
#        vastus="pikk"
#    else:
#         vastus="tundmatu"
#    print("Твой рост {0}".format(vastus))
#except :
#    print("Неправильный формат")
