import wolframalpha
import PySimpleGUI as sg
import wikipedia

app_id = '7PU8K2-TYL4XK4G5W'
client = wolframalpha.Client(app_id)


# ==========================gui code===========================================================
sg.theme('Black')   # Add a t ouch of color
# All the stuff inside your window.
layout = [[sg.Text('How May I Help', background_color='Black', text_color='Green')],
          [sg.Text('Ask Away')],
          [sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    wiki_res = wikipedia.summary(values[0], sentences=2)
    res = client.query(values[0])
    wolframa_res = next(res.results).text
    sg.Popup("WolframAlpha: " + wolframa_res, "WikiPedia: " + wiki_res)


window.close()
