import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.popup import Popup
from kivy.clock import Clock
import time
import os
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.carousel import Carousel


Window.size = (800, 600)
Window.clearcolor = (0.001,0,0,0)

def SpaceSound():
    sound1 = SoundLoader.load("SpaceRetardAudio//space.wav")
    if sound1:
        print("sound is found at %s"% sound1.source)
        print("sound length is %.3f seconds"%sound1.length)
        sound1.loop = True
        sound1.play()
#Sound01 = SpaceSound()                   REMOVE COMMENT


class FloatLayoutt(FloatLayout):
    pass
class PussyFloat(FloatLayout):
    PussyImg = Image()

#All Window Class and Function-                                       NEVER PUT ID OF .KV WITHIN QUOTE S ""
class StartUpStudios(Screen):
    def WinF(self):
        flt = FloatLayoutt()
        clr = Color()
        LogoImg = Image()

class MainWindow(Screen):

    def WinF(self):
        flt = FloatLayoutt()

    def PussyPops(self):
        psipp = PussyPop()

class DisclaimerWindow(Screen):
    def fltt(self):
        flt = FloatLayoutt()
        clr = Color()

class SecondWindow(Screen):

    def WinF(self):
        flt = FloatLayoutt()
        clr = Color()

    def Popss(self):
        sb = SubmitPop()

class ThirdWindow(Screen):
    def fltt(self):
        flt = FloatLayoutt()
        Wimg = Image()

class FourthWindow(Screen):
    p = 0
    def fltt(self):
        flt = FloatLayoutt()
        Wimg = Image()

    def PlusClickAdd(self):
        self.p = self.p+ 1
        self.ids.progress.value = self.p

class GameWindow(Screen):
    def plots(self):
        flt = FloatLayoutt()
        clr = Color()
        carousel = Carousel()

           #  })]                                                     #All Windows

def PussyPop():
    PsyPops = PussyFloat()
    PsiPp =  Popup(title= "Shame !" , content = PsyPops , size_hint=(None,None) , size = (350,450))
    PsiPp.open()

def SubmitPop():
    Fpops = FloatLayoutt()
    Pop =  Popup(title="Congrats! Retard", content=Fpops,size_hint=(None,None), size = (300,300))
    Pop.open()

class Screenmngr(ScreenManager):
    pass

kv = Builder.load_file("main.kv")
sm = Screenmngr()
Screens = [StartUpStudios(name="Fukeu"),
           MainWindow(name="main"),
           DisclaimerWindow(name="Disclaimer"),
           SecondWindow(name="Second"),
           ThirdWindow(name="Third"),
           FourthWindow(name="Fourth"),
           GameWindow(name= "gamewindow"),
           ]

for scrn in Screens:
    sm.add_widget(scrn)





class MyApp(App):
    def build(self):
        self.title = "SPACE RETARD"
        self.icon = "SpaceRetardImages//demo_icon.png"

        return sm
if __name__ == "__main__":
    MyApp().run()
