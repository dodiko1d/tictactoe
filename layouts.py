import PySimpleGUI as sg

main_layout = []
for row_index in range(3):
    main_layout.append([])
    for col_index in range(3):
        main_layout[row_index].append(f'button{row_index*3+col_index}')

