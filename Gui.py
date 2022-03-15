from optparse import Values
from tkinter import Button
from tkinter.tix import WINDOW
from typing import Text
import PySimpleGUI as sg
from Funktioner import * 
from Main import *

sg.theme('dark grey 10')

layout = [ [sg.Text('Welcome to the chatbot')], 
        [sg.Output(size=(100,50), key='-OUTPUT-')], 
        [sg.InputText()], 
        [sg.Button('Chat'), sg.Button('Exit')]]

window = sg.Window('Chatbot', layout)





while True:
    event, values = window.read(timeout=20)
    if event == 'Chat':
            print('User', values)
            if does_film_exists(values[0]) == True:
                    choose_info(values[0])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()