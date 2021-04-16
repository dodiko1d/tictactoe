import PySimpleGUI as sg

def buttons_update(window: sg.Window,event: str,stats: dict):
    for numb in range(9):
        if event == f'button_{numb}' and f'button_{numb}' not in stats['used_buttons']:
            if not stats['counter'] % 2:
                window[f'button_{numb}'].update('X',button_color=('#212121', '#EEFF47'))
            else:
                window[f'button_{numb}'].update('O',button_color=('#212121', '#EEFF47'))
            stats['counter'] += 1
            stats['used_buttons'] |= {f'button_{numb}'}