import pyautogui as py
import time
import turtle
import os.path
import os
from tkinter import *
import keyboard as kb



#Ventana
window = turtle.Screen()
window.title("spam")
window.bgcolor("black")
window.setup(width=800, height=500)
window.tracer(0)
window.bgpic("spam.gif")
window.cv._rootwindow.resizable(False, False)


#texto principal
txt = turtle.Turtle()
txt.color("white")
txt.hideturtle()
txt.goto(0, 0)


#Titulo
title_and_wm = turtle.Turtle()
title_and_wm.penup()
title_and_wm.hideturtle()
title_and_wm.goto(-398, -245)
title_and_wm.color("red")
title_and_wm.write("by: Carlos Acosta", font=("friz quadrata tt", 14, "normal"))


#Instruciones
funciona = turtle.Turtle()
funciona.color("white")
funciona.hideturtle()
funciona.penup()
funciona.goto(0, 120)

funciona.goto(0, 70)
funciona.write("Apreta f4 para saber como funciona", align="center", font=("JMHTypewriter-Thin", 26, "normal"))

#reinicios
reset = turtle.Turtle()
reset.color("white")
reset.hideturtle()
reset.penup()

txt.clear()
txt.write("Esperando para poder spamear ",
              align="center", font=("JMHTypewriter-Thin", 26, "normal"))

def core():
    f = open("textov3.txt", encoding="utf-8")
    for word in f:
        py.typewrite(word)
        py.press("enter")

def ejecutar():
    while True:
        core()
        if kb.is_pressed("esc"):
            break



def about():
    txt.clear()
    funciona.clear()
    funciona.goto(0, 60)
    funciona.write("Para comenzar a spamear aprieta, f2 ", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    funciona.goto(0, 120)
    funciona.write("Para cerrar el programa aprieta, f3 ", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    funciona.goto(0, 0)
    funciona.write("Para modificar el archivo aprieta f1", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    funciona.goto(0, -100)
    funciona.write("para salir de aqui aprieta, f5", align="center", font=("JMHTypewriter-Thin", 26, "normal"))



def comenzar():
    if os.path.exists("textov3.txt"):
        pass

    else:
        txt.clear()
        txt.goto(0, 10)
        txt.write("No tienes el archivo correspondiente ", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
        txt.goto(0, -50)
        txt.write("Se procedera a crear el archivo", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
        time.sleep(3.5)
        file = open("textov3.txt", "a")
        file.close()


    if os.stat("textov3.txt").st_size == 0:
        txt.clear()
        txt.goto(0, 10)
        txt.write("Aprieta F1 para modificar el archivo ",align="center", font=("JMHTypewriter-Thin", 26, "normal"))
        txt.goto(0, -60)
        txt.write("y poder empezar espamear", align="center", font=("JMHTypewriter-Thin", 26, "normal"))




    else:
        txt.clear()
        funciona.clear()
        txt.write("Has comenzado a spamear",
                  align="center", font=("JMHTypewriter-Thin", 26, "normal"))
        time.sleep(2.5)
        ejecutar()
        time.sleep(1.5)
        txt.clear()
        txt.write("Has dejado de spamear ",
                  align="center", font=("JMHTypewriter-Thin", 26, "normal"))
        time.sleep(2)
        txt.clear()
        txt.write("Esperando para poder spamear ",
                  align="center", font=("JMHTypewriter-Thin", 26, "normal"))
        funciona.penup()
        funciona.goto(0, 120)

        funciona.goto(0, 70)
        funciona.write("Apreta f4 para saber como funciona", align="center", font=("JMHTypewriter-Thin", 26, "normal"))

def parar():
    txt.clear()
    funciona.clear()
    txt.penup()
    txt.goto(0, 50)
    txt.write("Gracias por usar el servicio de spam ",
              align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    txt.goto(0, -50)
    txt.write("Que le vaya muy bien", align="center"
                , font=("JMHTypewriter-Thin", 26, "normal"))
    time.sleep(5)
    window.bye()

def exit():
    txt.clear()
    title_and_wm.clear()
    funciona.clear()
    time.sleep(1.5)
    reset.penup()
    reset.goto(0, -50)
    reset.write("reiniciando todo, un momento ", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    time.sleep(2)
    reset.clear()
    reset.write("0%", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    time.sleep(2)
    reset.clear()
    reset.write("10%", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    title_and_wm.penup()
    title_and_wm.goto(-398, -245)
    title_and_wm.color("red")
    title_and_wm.write("by: Carlos Acosta", font=("courier", 14, "normal"))
    time.sleep(2)
    reset.clear()
    funciona.goto(0, 120)

    funciona.goto(0, 70)
    funciona.write("Apreta f4 para saber como funciona", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    reset.write("60%", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    time.sleep(2)
    txt.goto(0, 0)
    txt.write("Esperando para poder spamear ",
              align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    time.sleep(2)
    reset.clear()
    reset.write("100%", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    reset.penup()
    reset.goto(0, -80)
    reset.write("Reinicio completo ", align="center", font=("JMHTypewriter-Thin", 26, "normal"))
    time.sleep(3)
    reset.clear()

def modified():
    f2 = open("textov3.txt", "w", encoding="utf8")
    txt3 = py.prompt("Inserta loque quieres spamear", "TEXTO A ESPAMEAR")
    f2.write(txt3)
    f2.close()

kb.add_hotkey("f2", comenzar)

window.listen()
window.onkeypress(comenzar, "F2")
window.onkeypress(parar, "F3")
window.onkeypress(about, "F4")
window.onkeypress(exit, "F5")
window.onkeypress(modified, "F1")

window.mainloop()