import PySimpleGUI as sg
layout_main = []

window = sg.Window('Крестики-нолики', layout=layout_main)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'button_1':
        window['button_1'].update(button_color=('#ffffff', '#212121'))

window.close()

