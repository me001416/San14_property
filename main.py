import tkinter as tk
# import tkFont as tf
import json
from typing import List, Dict, Any

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
                        formatted_str += f"{sub_key} : {inner_value} "
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

    index = 0

    scrollX = tk.Scrollbar(window, orient='horizontal')
    scrollX.pack(side='bottom', fill='x')

    scrollY  = tk.Scrollbar(window, orient='vertical')
    scrollY .pack(side='right', fill='y')

    # listbotx_font = tk.Font(size = 24)

    new_Listbox = tk.Listbox( window, height=100, width=150, xscrollcommand=scrollX.set, yscrollcommand=scrollY.set, font=(14) )

    scrollX.config(command=new_Listbox.xview)
    scrollY.config(command=new_Listbox.yview)

    for item in Json_list :
        # print(item)

        new_Listbox.insert( index, item )
        new_Listbox.place(x=0,y=100)

        index += 1

    window.mainloop()