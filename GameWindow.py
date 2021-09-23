import kivy
import time
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.carousel import Carousel
from kivy.graphics  import Color
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ToggleButtonBehavior                #this is for the control over radio button

Window.size = (850,600)
Window.fullscreen=False
Config.set('graphics', 'resizable', False)
                                                                    # Make the PopUp Window // Then Make the FIrst Storyline Window in main.py

class GameWindow001(Screen):
    def ExitCode(self):
        exit()
    def plot(self):
        flt = FloatLayout()
        bxlt = BoxLayout()
        clr = Color()
        carousel = Carousel()

    def StartStory(self):
        glide = '''You have one hour to go to your exam hall. \n
You are in your House. \n
Your Father is milking your mother in the next room. \n                    
Your bus will arrive in 10 minutes. \n
What do you want to do in the mean time ?
        '''
        self.ids.story.text = glide                                              #'include On_press_Enter Function for GameInput'

    def Options(self):
        self.ids.opt1.text = "♥ Check if you packed all the equipments"
        self.ids.opt2.text = "♥ Sneak into your parents room"
        self.ids.opt3.text = "♥ Go to the Bathroom"
        self.ids.opt4.text = "♥ Wait for the Bus doing nothing"


class GameWindow002(Screen):
    def ExitCode(self):
        exit()

    def plot(self):
        flt = FloatLayout()
        bxlt = BoxLayout()
        clr = Color()
        carousel = Carousel()

    def StartStory(self):
        glide = '''You have open your bag 
and see a dead cockroach and a dirty eraser.
~
            '''
        self.ids.story.text = glide

    def Options(self):
        self.ids.opt1.text = "♥ Add items(Pencil, Pen, Pencil Sharpner)"
        self.ids.opt2.text = "♥ Clean the cockroach"
        self.ids.opt3.text = "♥ Eat the cockroach"
class GameWindow003(Screen):
    pass

class Screenmanager(ScreenManager):
    pass
kv = Builder.load_file("gamewindow.kv")
sm = Screenmanager()
GameScreens = [GameWindow001(name= "GameWindow001"),
               GameWindow002(name= "GameWindow002"),
               GameWindow003(name= "GameWindow003"),





               ]

for screen in GameScreens:
    sm.add_widget(screen)


class GamewindowApp(App):
    def build(self):
        self.title = "GameWIndow"
        return sm

GamewindowApp().run()
