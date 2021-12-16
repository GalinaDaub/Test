from kivy.app import App

from kivy.uix.modalview import ModalView

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 960)
Config.set('graphics', 'height', 480)

def label_func(modal_name, position_x, position_y): #функция для лейбла кнопок
	label = Label(
        text=modal_name, 
        font_size='50sp', 
        halign='center', 
        valign='middle', 
        size_hint=(0.3, 0.2), 
        pos_hint={
        'center_x': position_x, 
        'y': position_y}
        )
	return label

def btn_open_func(button_name, position_x, position_y): #функция для кнопок
	btn_open = Button(
        text=button_name, 
        size_hint=(0.15, 0.3), 
        pos_hint={
        'center_x': position_x, 
        'center_y':position_y}
        )
	return btn_open
	

class MainpApp(App):
    def build(self):
		
        fl = FloatLayout(size_hint=[1, 1])
        
        modal = ModalView(
        size_hint=(1, 1), 
        auto_dismiss=False
        )
        
        fl_into = FloatLayout(size_hint=(.9, .9))
                        
        btn_close = Button(
        text='X', 
        size_hint=(0.06, 0.1), 
        pos_hint={
        'center_x':0.99, 
        'y':.95}
        )
        btn_close.bind(on_press=modal.dismiss)
        
        label_avatar = label_func('твoй аватар', 0.5, 0.9)

        fl_into.add_widget(label_avatar)
        fl_into.add_widget(btn_close)
        
        modal.add_widget(fl_into)
        
        btn_avatar = btn_open_func('аватар', 0.08, 0.83)
        btn_avatar.bind(on_press = modal.open)
        
        fl.add_widget(btn_avatar)
       
        return fl
        
if __name__ == '__main__':
	MainpApp().run()
