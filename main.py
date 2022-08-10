import threading
import shutil
import plyer
import core
import os

from kivymd.app import MDApp

from kivy.utils import get_color_from_hex as getc
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.clock import Clock

from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.label import MDLabel
from kivymd.utils.fitimage import FitImage

filepath_cache = None
resultdirectory_cache = None

class WindowsManager(ScreenManager):
    pass

class WelcomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.changeScreen, 2)
    def changeScreen(self, _):
        self.manager.transition = FadeTransition()
        self.manager.current = "selectimage"

class SelectImage(Screen):
    def ChooseImage(self):
        global filepath_cache
        file_path = plyer.filechooser.open_file()[0]
        if not file_path.split(".")[-1] in ("jpg", "png"):
            return
        filepath_cache = file_path
        self.manager.transition = FadeTransition()
        self.manager.current = "loading"

class Loading(Screen):
    def on_pre_enter(self):
        self.ids.progress.start()
        self.loadingThread = threading.Thread(target = self.loadFilters)
        self.loadingThread.start()
    def loadFilters(self):
        global resultdirectory_cache
        resultdirectory_cache = core.LoadAllFilters(filepath_cache)
        Clock.schedule_once(self.changeScreen)
    def changeScreen(self, dt):
        self.manager.current = "showresult"
        
        

class ShowResult(Screen):
    def on_pre_enter(self):
        images = os.listdir(resultdirectory_cache)
        images_paths = list(map(lambda image_path: os.path.join(resultdirectory_cache, image_path) , images))
        for index ,image in enumerate(images_paths):
            item = MDSwiperItem(orientation = "vertical")
            item.add_widget(FitImage(source = image, radius=[30]))
            item.add_widget(MDLabel(text = images[index].rsplit(".", 1)[0], size_hint_y = 0.05, halign = "center"))
            self.ids.ResultList.add_widget(item)

class MainApp(MDApp):
    def build(self):
        Builder.load_file("design.kv")
        Window.clearcolor = getc("#F36F6F")
        Window.title = "Filtergram"
        Window.size = (1100, 600)
        
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.accent_palette = "Blue"
        
        return WindowsManager()

if __name__ == "__main__":
    MainApp().run()
    th_cleanup = threading.Thread(target = shutil.rmtree, args=(resultdirectory_cache,))
    th_cleanup.start()
    th_cleanup.join()
