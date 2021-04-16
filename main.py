import PySimpleGUI as sg
from stats import stats
from layout import layout
from buttons_update import buttons_update


def main():
    window = sg.Window('Крестики-нолики', layout=layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        buttons_update(window, event, stats)
    window.close()


if __name__ == '__main__':
    main()
