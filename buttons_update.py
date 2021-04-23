import PySimpleGUI as sg
from board import win

def buttons_update(window: sg.Window,event: str,stats: dict):
    for numb in range(9):
        button_row=numb//3
        button_col=numb%3
        if event == f'button_{numb}' and f'button_{numb}' not in stats['used_buttons']:
            if not stats['counter'] % 2:
                window[f'button_{numb}'].update('X',button_color=('#212121', '#EEFF47'))
                stats['field'][button_row][button_col] = 'X'
            else:
                window[f'button_{numb}'].update('O',button_color=('#212121', '#EEFF47'))
                stats['field'][button_row][button_col] = 'O'
            stats['counter'] += 1
            stats['used_buttons'] |= {f'button_{numb}'}
            winner = win(stats['field'])
        if winner == 'D' and stats['counter'] < 9
            print('Draw.')
        else:
            print(f'Winner is {winner}.')