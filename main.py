import tkinter as tk
import json
from typing import List, Dict, Any
from property import *

flag_dict = {
    'show_damage' : False,
    'enemy_morale_down' : False,
    'chaos' : False,
    'arson' : False
}

def load_json(file_path: str) -> dict:
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data.

    Example:
        >>> data = load_json('san14.json')
        >>> print(data)
        {'key': 'value'}

    繁體中文：
    從指定檔案載入 JSON 資料並解析為字典格式。
    """
    try:
        # 開啟檔案並載入 JSON 資料
        with open(file_path, 'r', encoding="utf-8") as srcF:
            srcJson = json.load(srcF)
        return srcJson
    except FileNotFoundError as e:
        # 處理檔案找不到的例外情況
        raise FileNotFoundError(f"檔案未找到：{file_path}") from e
    except json.JSONDecodeError as e:
        # 處理 JSON 格式錯誤的例外情況
        raise ValueError(f"無法解析 JSON 格式：{file_path}") from e

def parse_dictionary(source_json: Dict[str, Any]) -> List[str]:
    """
    Parse a nested dictionary and format its content into a list of strings.

    Args:
        source_json (Dict[str, Any]): 
            A dictionary where keys are strings and values are either strings, dictionaries, or other nested structures.
            
            Example:
            {
                "key1": {
                    "attribute1": "value1",
                    "attribute2": {"效果": "有效", "attribute3": "value3"}
                },
                "key2": {"attribute4": "value4"}
            }

    Returns:
        List[str]: A list of formatted strings representing the parsed dictionary content.

        Example Output:
        [
            "key1    : attribute1 : value1 attribute2 : 有效 attribute3 : value3 ",
            "key2    : attribute4 : value4 "
        ]
    """
    # 初始化結果列表
    result = []
    
    for key, value in source_json.items():
        # 建立每個主鍵的輸出字串
        formatted_str = key
        formatted_str += '  ' * (4 - len(key))  # 對齊用的空白
        formatted_str += " : "
        
        # 遍歷主鍵對應的值
        for sub_key, sub_value in value.items():
            if sub_key == '對據點':  # 忽略名為 "對據點" 的鍵
                continue
            
            # 處理子屬性為字串的情況
            if isinstance(sub_value, str):
                formatted_str += f"{sub_key} : {sub_value} "
            # 處理子屬性為字典的情況
            elif isinstance(sub_value, dict):
                if sub_value.get('效果') == 'N/A':  # 如果效果為 'N/A'，直接標記並跳過詳細處理
                    formatted_str += f"{sub_key} : N/A "
                    continue
                # 遍歷內層字典
                for inner_key, inner_value in sub_value.items():
                    if inner_key == '效果':
                        formatted_str += f"{sub_key} : [{inner_value}] "
                    elif isinstance(inner_value, (str, int)):  # 處理字串或整數
                        formatted_str += f"{inner_key} : {inner_value} "
        
        # 將格式化的字串加入結果列表
        result.append(formatted_str)
    
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

def create_window() -> tk.Tk:
    """
    Create and configure a Tkinter window for the game "三國志14 戰法".

    This function initializes a Tkinter window with the specified title, dimensions, 
    and resizing properties.

    Returns:
        tk.Tk: The configured Tkinter window.

    Example:
        window = create_game_window()
        window.mainloop()
    """
    # 初始化 Tkinter 視窗
    window = tk.Tk()
    
    # 設定視窗標題
    window.title('三國志14 戰法')
    
    # 設定視窗尺寸
    window.geometry('380x400')
    
    # 設定視窗大小可調整
    window.resizable(True, True)  # 允許水平與垂直調整
    
    return window

if __name__ == '__main__':

    window = create_window()

    srcJson = load_json('san14.json')

    Json_list = parse_dictionary(srcJson)

    scrollX = tk.Scrollbar(window, orient='horizontal')
    scrollX.pack(side='bottom', fill='x')

    scrollY  = tk.Scrollbar(window, orient='vertical')
    scrollY .pack(side='right', fill='y')

    new_Listbox = tk.Listbox( window, height=250, width=150, xscrollcommand=scrollX.set, yscrollcommand=scrollY.set, font=(14) )

    scrollX.config(command=new_Listbox.xview)
    scrollY.config(command=new_Listbox.yview)

    for item in Json_list :
        new_Listbox.insert( tk.END, item )

    provoke = True  # 挑釁
    status_abnormality_removal = True  # 異常狀態解除
    durability_damage = True  # 城池耐久損傷
    enemy_all_stats_decrease = True  # 敵方全能力降低
    our_all_stats_increase = True  # 我方全能力上升
    enemy_full_status_abnormality = True  # 敵方全狀態異常
    # 我方機動上升
    # 我方防禦上升

    button_1 = tk.Button(text='傷害',        bg='#FF4040', font=(14))
    button_2 = tk.Button(text='敵方士氣降低', bg='#FF4040', font=(14))
    button_3 = tk.Button(text='混亂',        bg='#FF4040', font=(14))
    button_4 = tk.Button(text='放火',        bg='#FF4040', font=(14))
    button_5 = tk.Button(text='止步',        bg='#FF4040', font=(14))
    button_6 = tk.Button(text='我方士氣上升',        bg='#FF4040', font=(14))
    button_7 = tk.Button(text='我方攻軍上升', bg='#FF4040', font=(14))
    button_8 = tk.Button(text='我方破城上升', bg='#FF4040', font=(14))
    button_9 = tk.Button(text='敵方攻軍降低', bg='#FF4040', font=(14))
    button_10 = tk.Button(text='敵方攻城降低', bg='#FF4040', font=(14))
    button_11 = tk.Button(text='敵方破城降低', bg='#FF4040', font=(14))
    button_12 = tk.Button(text='敵方防禦降低', bg='#FF4040', font=(14))
    button_13 = tk.Button(text='敵方機動降低', bg='#FF4040', font=(14))
    button_14 = tk.Button(text='傷兵回復', bg='#FF4040', font=(14))
    button_15 = tk.Button(text='挑釁', bg='#FF4040', font=(14))
    button_16 = tk.Button(text='異常狀態解除', bg='#FF4040', font=(14))
    button_17 = tk.Button(text='城池耐久損傷', bg='#FF4040', font=(14))
    button_18 = tk.Button(text='敵方全能力降低', bg='#FF4040', font=(14))
    button_19 = tk.Button(text='我方全能力上升', bg='#FF4040', font=(14))
    button_20 = tk.Button(text='敵方全狀態異常', bg='#FF4040', font=(14))
    button_21 = tk.Button(text='我方機動上升', bg='#FF4040', font=(14))
    button_22 = tk.Button(text='我方防禦上升', bg='#FF4040', font=(14))

    fm = FlagManager()
    fm.set_json_list(Json_list)
    fm.set_new_Listbox(new_Listbox)

    foo1 = lambda: fm.toggle_button( button_1, 0 )
    button_1.config( command=foo1 )

    foo2 = lambda: fm.toggle_button( button_2, 1 )
    button_2.config( command=foo2 )

    foo3 = lambda: fm.toggle_button( button_3, 2 )
    button_3.config( command=foo3 )

    foo4 = lambda: fm.toggle_button( button_4, 3 )
    button_4.config( command=foo4 )

    foo5 = lambda: fm.toggle_button( button_5, 4 )
    button_5.config( command=foo5 )

    foo6 = lambda: fm.toggle_button( button_6, 5 )
    button_6.config( command=foo6 )

    foo7 = lambda: fm.toggle_button(button_7, 6)
    button_7.config(command=foo7)

    foo8 = lambda: fm.toggle_button(button_8, 7)
    button_8.config(command=foo8)

    foo9 = lambda: fm.toggle_button(button_9, 8)
    button_9.config(command=foo9)

    foo10 = lambda: fm.toggle_button(button_10, 9)
    button_10.config(command=foo10)

    foo11 = lambda: fm.toggle_button(button_11, 10)
    button_11.config(command=foo11)

    foo12 = lambda: fm.toggle_button(button_12, 11)
    button_12.config(command=foo12)

    foo13 = lambda: fm.toggle_button(button_13, 12)
    button_13.config(command=foo13)

    foo14 = lambda: fm.toggle_button(button_14, 13)
    button_14.config(command=foo14)

    foo15 = lambda: fm.toggle_button(button_15, 14)
    button_15.config(command=foo15)

    foo16 = lambda: fm.toggle_button(button_16, 15)
    button_16.config(command=foo16)

    foo17 = lambda: fm.toggle_button(button_17, 16)
    button_17.config(command=foo17)

    foo18 = lambda: fm.toggle_button(button_18, 17)
    button_18.config(command=foo18)

    foo19 = lambda: fm.toggle_button(button_19, 18)
    button_19.config(command=foo19)

    foo20 = lambda: fm.toggle_button(button_20, 19)
    button_20.config(command=foo20)

    foo21 = lambda: fm.toggle_button(button_21, 20)
    button_21.config(command=foo21)

    foo22 = lambda: fm.toggle_button(button_22, 21)
    button_22.config(command=foo22)

    new_Listbox.place(x=0,y=100)
    button_1.place(x=0, y=0)
    button_2.place(x=65, y=00)
    button_3.place(x=210, y=00)
    button_4.place(x=275, y=00)
    button_5.place(x=340, y=00)
    button_6.place(x=405, y=00)
    button_7.place(x=550, y=0)
    button_8.place(x=695, y=0)
    button_9.place(x=0, y=50)
    button_10.place(x=145, y=50)
    button_11.place(x=290, y=50)
    button_12.place(x=435, y=50)
    button_13.place(x=580, y=50)
    button_14.place(x=725, y=50)
    button_15.place(x=840, y=0)
    button_16.place(x=0, y=100)
    button_17.place(x=145, y=100)
    button_18.place(x=290, y=100)
    button_19.place(x=455, y=100)
    button_20.place(x=620, y=100)
    button_21.place(x=765, y=100)
    button_22.place(x=900, y=100)

    window.mainloop()