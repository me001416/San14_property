from San14_property.main import refresh_listbox

class FlagManager:
    def __init__( self ):
        self.flag_list = {
            'show_damage': False,
            'enemy_morale_down': False,
            'chaos': False,
            'arson': False
        }

    def toggle_button( self, src_button, flag ):
        # 自定義按鈕切換邏輯
        self.button_color( self, src_button, flag )

    def button_color( self, src_button, flag ):
        if flag:
            src_button.config(bg='#FF4040')
        else:
            src_button.config(bg='#FFD39B')

        refresh_listbox()
