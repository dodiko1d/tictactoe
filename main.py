import PySimpleGUI as sg
layout_main = []

window = sg.Window('Крестики-нолики', layout=layout_main)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

