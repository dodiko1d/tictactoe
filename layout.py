import PySimpleGUI as sg


layout = [
    [sg.Button(key=f'button_{x * 3 + z}', size=(30, 9), button_color=('#212121', '#ffffff')) for z in range(3)] for x in range(3)
]

layout += [[sg.Button('', key='winner', visible=False)]]
