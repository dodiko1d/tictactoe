from layouts.main import layout_main
import PySimpleGUI as sg


window = sg.Window('Крестики-нолики', layout=layout_main)


counter = 1
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'button_1' and counter % 2:
        window['button_1'].update(button_color=('#ffffff', '#212121'))
        counter += 1
    elif event == 'button_1' and not counter % 2:
        window['button_1'].update(button_color=('#212121', '#ffffff'))
        counter += 1
    print('Hello, World')
window.close()

