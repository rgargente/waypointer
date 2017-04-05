import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')  # replace with your current kivy version !


class WaypointerWidget(BoxLayout):
    result_lbl = ObjectProperty(None)
    waypoint_had = ObjectProperty(None)
    position_had = ObjectProperty(None)

    def guideme_click(self):
        heading = self.waypoint_had.heading
        dist = self.position_had.dist
        self.result_lbl.text = \
            'Go {}º for {} km'.format(heading, dist)


class WaypointerApp(App):
    def build(self):
        return WaypointerWidget()


if __name__ == '__main__':
    WaypointerApp().run()
