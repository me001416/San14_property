import tkinter as tk
import json

def json_load():
    with open('san14.json', 'r', encoding="utf-8") as srcF:
        srcJson = json.load(srcF)

    # print(srcJson)
    # print(type(srcJson))

    return srcJson

def dict_parse(srcJson):
    result =[]

    for key, value in srcJson.items() :
        temp_str = key
        temp_str += '  ' * ( 4 - len(key) )
        temp_str += "{}".format( ' : ' )
        # print(key)
        # print(len(key))
        # print(value)
        # print(type(key))
        # print(type(value))
        # print('')

        for key1, value1 in value.items() :
            # print(key1)
            # print(value1)
            # print(type(key1))
            # print(type(value1))
            if type(value1) is str :
                temp_str += key1 + " : " + value1 + ' '
            if type(value1) is dict :
                for key2, value2 in value1.items() :
                    # print(key2)
                    # print(value2)
                    # print(type(key2))
                    # print(type(value2))
                    if type(value2) is str :
                        temp_str += key2 + " : " + value2
                    if type(value2) is int :
                        temp_str += key2 + " : " + str(value2)

        result.append(temp_str)

    return result


def json_data_generate():
    san14_data = {
        "奮戰" :
        {
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
        },
        "突擊" :
        {
            "系統" : "",
            "對應能力" : "",
            "對據點" : "",
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
                "效果" : "N/A",
                "範圍" : 0,
                "威力" : 0,
                "時間" : 0
            }
        }
    }

    with open("san14_test.json", 'w', encoding="utf-8") as f:
        json.dump(san14_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':

    window = tk.Tk()
    window.title('三國志14 戰法')
    window.geometry('380x400')
    window.resizable(True, True)
    # window.iconbitmap('icon.ico')

    srcJson = json_load()
    # json_data_generate()

    Json_list = dict_parse(srcJson)

    index = 0

    new_Listbox = tk.Listbox( window, height=200, width=200 )

    scrollX = tk.Scrollbar(window, orient='horizontal')
    scrollX.pack(side='bottom', fill='x')
    scrollX.config(command=new_Listbox.xview)

    scrollY  = tk.Scrollbar(window, orient='vertical')
    scrollY .pack(side='right', fill='y')
    scrollY .config(command=new_Listbox.yview)

    for item in Json_list :
        # print(item)

        new_Listbox.insert( index, item )
        new_Listbox.place(x=0,y=100)

        index += 1

    window.mainloop()