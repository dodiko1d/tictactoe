import PySimpleGUI as sg


layout = [
    [sg.Button(key=f'button_{x * 3 + z}', size=(30, 9), button_color=('#212121', '#ffffff')) for z in range(3)] for x in range(3)
]

layout += [[sg.Text('', key='winner', visible=False, font=("Helvetica", 32), size=(50, 3))],
           [sg.Button('Restart', key='restart', visible=False)]]
