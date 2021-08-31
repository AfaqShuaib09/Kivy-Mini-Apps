from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window



class GreetApp(App):
    App.title = 'Kivy Greeting App'
    Window.size = (400, 600)


class userInterface(GridLayout):
    def greet(self, widget, widget2, msg):
        msg.strip()
        if msg == '' or len(msg)==0:
            widget2.text = "What's your name?"
        else:
            widget2.text = f'Hello {msg}!'
    pass


if __name__ == "__main__":
    GreetApp().run()
