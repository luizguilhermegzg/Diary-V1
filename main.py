########################################################              IMPORTANT DISCLAIMER!!!!!!!!!!!!!!!!!!!                  ###################################################################
# The program have a bug unsolved in the "OPEN" interation function. The bug is:  When you click in any button of the window without selecting a path the program close automaticaly.
# If you know and wanna solve this problem, please make a pull request, i will verify and push to the main project if the problem be solved. Thank you all!
########################################################              IMPORTS                  ###################################################################

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText, WIN_CLOSED, Window
sg.theme('Reddit')

########################################################              WINDOWS                  ###################################################################
def diary_window():
    layout= [
         [sg.Button('NEW', size=(7,1), font='book-antiqua 14', button_color='#658EA9'), sg.Button('SAVE', size=(7,1), font='book-antiqua 14', button_color='#88B2CC'), sg.Button('OPEN', size=(7,1), font='book-antiqua 14', button_color='#E7D4C0'), sg.Button('DELETE', size=(7,1), font='book-antiqua 14', button_color='#E98973'), sg.Text('This software was created by Cricket Softwares and Services', background_color='aquamarine')],
         [sg.Multiline(size=(120, 30), key='textbox', font='calibri 12', background_color='#E7F2F8')]
    ]
    screen = sg.Window('Diary V1', layout, background_color='aquamarine').finalize()
    interations(screen)


def open_new_archive(text):
    layout= [
        [sg.Button('NEW', size=(7,1), font='book-antiqua 14', button_color='#658EA9'), sg.Button('SAVE', size=(7,1), font='book-antiqua 14', button_color='#88B2CC'), sg.Button('OPEN', size=(7,1), font='book-antiqua 14', button_color='#E7D4C0'), sg.Button('DELETE', size=(7,1), font='book-antiqua 14', button_color='#E98973'), sg.Text('This software was created by Cricket Softwares and Services', background_color='aquamarine')],
        [sg.Multiline(text ,size=(120, 30), key='textbox', font='calibri 12', background_color='#E7F2F8')]
    ]
    screen = sg.Window("Diary V",layout, background_color='aquamarine').finalize()
    interations(screen)


########################################################              CATCHING EVENTS, VALUES AND ETC                  ###################################################################
def interations(window):
    while True:
        events, values = window.read()
        if events == sg.WIN_CLOSED:
            break
        if events == 'NEW':
            diary_window()
        if events == 'SAVE':
                path = sg.PopupGetFolder('Choose a folder to save:')
                if path == "":
                    print('nada')
                else: 
                    file_name_layout = [[sg.Text('Say the name of your file:'), sg.InputText(key='file_name'), sg.Button('Save')]]
                    file_name_window = sg.Window('File name', file_name_layout)
                    while True:
                        file_events, file_values = file_name_window.read()
                        if file_events == sg.WIN_CLOSED:
                            break
                        if file_events == 'Save' and file_values['file_name'] != "":
                            my_file = open(path +'/'+ file_values['file_name']+ '.txt','w')
                            my_file.write(values['textbox'])
                            sg.popup_notify("Arquivo salvo com sucesso!!!")
                            my_file.close() 
                            file_name_window.close()
                        else:
                            sg.popup_error("You need to put a name!!!")
        if events == 'OPEN':                              ## Problem to solve here!!!
            filename= open(sg.popup_get_file('Enter the file you wish to process'))
            if filename == "" or filename == None:
                print('nada')
            else:
                extracted_text = filename.read()
                window.close()
                open_new_archive(extracted_text)
        if events == 'DELETE':
            window.close()
            open_new_archive('')
########################################################              CALL MAIN WINDOW                  ###################################################################
diary_window()









