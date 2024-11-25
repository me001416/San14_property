import tkinter as tk
import json

window = tk.Tk()
window.title('三國志14 戰法')
window.geometry('380x400')
window.resizable(False, False)
# window.iconbitmap('icon.ico')

with open('san14.json', 'r') as srcF:
    srcJson = json.load(srcF)

print(srcJson)

# window.mainloop()