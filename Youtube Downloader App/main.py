from kivy.properties import StringProperty
from pytube import YouTube
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    string = StringProperty('Paste your link below')
    def download_vedio_from_link(self, link, widget):
        SAVE_PATH = "C:\yt_vedieos" #paste the path here where you want the file to be stored
        yt_link = link
        try:
            yt = YouTube(link)
        except:
            print("Connection Error")
        print(yt.title)
        stream = yt.streams.get_lowest_resolution()
        stream.download(SAVE_PATH)
        widget.text = 'Task Completed!'
    pass


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class MyApp(App):
    App.title = 'Youtube Vedio Downloader App'
    Window.size = (400, 600)
    pass


if __name__ == "__main__":
    MyApp().run()
