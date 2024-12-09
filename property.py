class FlagManager:
    def __init__(self):
        self.flag_dict = {
            'show_damage': False,
            'enemy_morale_down': False,
            'chaos': False,
            'arson': False
        }

    def toggle_button(self, src_button, flag):
        # 自定義按鈕切換邏輯
        button_color(src_button, flag)
