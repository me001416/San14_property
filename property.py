import tkinter as tk

class FlagManager:
    def __init__( self ):
        self.flag_list = [
            [True, '傷害'],
            [True, '敵方士氣降低'],
            [True, '混亂'],
            [True, '放火']
        ]
        self.Json_list = None
        self.new_Listbox = None

    def toggle_button( self, src_button, index ):
        self.flag_list[index][0] = not self.flag_list[index][0]

        # 自定義按鈕切換邏輯
        self.button_color( src_button, self.flag_list[index][0] )

    def button_color( self, src_button, flag ):
        if flag:
            src_button.config(bg='#FF4040')
        else:
            src_button.config(bg='#FFD39B')

        self.refresh_listbox()

    def return_value( self, index ):
        return self.flag_list[index][0], self.flag_list[index][1]

    def set_json_list( self, src ):
        self.Json_list = src

    def set_new_Listbox( self, src ):
        self.new_Listbox = src

    def check_line( self, src ):
        ret = False

        for item in self.flag_list:
            if item[1] in src and not item[0]:
                ret = True
                break
        
        return ret

    def refresh_listbox( self ):

        filtered_items = []

        for line in self.Json_list:
            if self.check_line( line ):
                continue
            
            filtered_items.append( line )

        # Clear the Listbox first
        self.new_Listbox.delete( 0, tk.END )

        for item in filtered_items:
            self.new_Listbox.insert( "end", item )
