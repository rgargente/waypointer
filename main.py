import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')  # replace with your current kivy version !


class WaypointerWidget(BoxLayout):
    pass


class WaypointerApp(App):
    def build(self):
        return WaypointerWidget()


if __name__ == '__main__':
    WaypointerApp().run()
