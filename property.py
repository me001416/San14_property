from main import refresh_listbox
import tkinter as tk

class FlagManager:
    def __init__( self ):
        self.flag_list = [
            ['show_damage', False, '傷害'],
            ['enemy_morale_down', False, '敵方士氣降低'],
            ['chaos', False, '混亂'],
            ['arson', False, '放火']
        ]
        self.Json_list
        self.new_Listbox

    def toggle_button( self, src_button, index ):
        # 自定義按鈕切換邏輯
        self.button_color( src_button, self.flag_list[index][1] )

    def button_color( self, src_button, flag ):
        if flag:
            src_button.config(bg='#FF4040')
        else:
            src_button.config(bg='#FFD39B')

        self.refresh_listbox()

    def return_value( self, index ):
        return self.flag_list[index][1], self.flag_list[index][2]

    def set_json_list( self, src ):
        self.Json_list = src

    def set_new_Listbox( self, src ):
        self.new_Listbox = src

    def refresh_listbox( self ):

        filtered_items = []

        for line in self.Json_list:
            for item in self.flag_list:
                if item[2] in line and not item[1]
            if "[傷害]" in line and not show_damage:
                continue

            if "[敵方士氣降低]" in line and not enemy_morale_down:
                continue

            if "[混亂]" in line and not chaos:
                continue

            if "[放火]" in line and not arson:
                continue

            filtered_items.append( line )

        # Clear the Listbox first
        self.new_Listbox.delete( 0, tk.END )

        for item in filtered_items:
            self.new_Listbox.insert( "end", item )
