from random import randint,shuffle
from tkinter import *
from string import *

pencere=Tk()
pencere.title("Şifre Oluşturucu")

sifre_text=Label(text="Şifre",fg="dark green",bg="cyan",font="Times 30 bold")
sifre_text.pack()

rakamlar=digits
semboller=punctuation
kucuk_harf=ascii_lowercase
buyuk_harf=ascii_uppercase
password=[rakamlar,semboller,kucuk_harf,buyuk_harf]
sifre=""
text_sifre=""

for i in range(4):
    for p in range(2):
        sifre+=password[p][randint(0,9)]
sifre=list(sifre)
shuffle(sifre)
for z in sifre:
    text_sifre+=z

def olustur():
    sifre_text.config(text=text_sifre)


sifre_button=Button(text="Şifre Oluştur",fg="blue",bg="light green",font="Times 30 bold",activebackground="pink",cursor="plus",command=olustur)
sifre_button.pack()


pencere.mainloop()
