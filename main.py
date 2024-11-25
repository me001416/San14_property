import tkinter as tk
import json

def json_load():
    with open('san14.json', 'r') as srcF:
        srcJson = json.load(srcF)

    print(srcJson)

def json_data_generate():
    san14_data = {
        "戰法" : "奮戰",
        "系統" : "攻擊",
        "對應能力" : "武力",
        "對據點" : "-",
        "發動時間" : "12日",
        "效果一" :
        {
            "效果" : "傷害",
            "範圍" : 1,
            "威力" : 10,
            "時間" : 0
        },
        "效果二" : 
        {
            "效果" : "-",
            "範圍" : 0,
            "威力" : 0,
            "時間" : 0
        }
    }

if __name__ == '__main__':

    window = tk.Tk()
    window.title('三國志14 戰法')
    window.geometry('380x400')
    window.resizable(False, False)
    # window.iconbitmap('icon.ico')

    # json_load()
    json_data_generate()


    # window.mainloop()