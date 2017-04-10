import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from vector import Vector

kivy.require('1.9.1')  # replace with your current kivy version !


class WaypointerWidget(BoxLayout):
    result_lbl = ObjectProperty(None)
    waypoint_vector = ObjectProperty(None)
    position_vector = ObjectProperty(None)

    def guideme_click(self):
        waypoint_vector = Vector(float(self.waypoint_vector.heading), float(self.waypoint_vector.range))
        position_vector = Vector(float(self.position_vector.heading), float(self.position_vector.range))
        course_vector = Vector.get_course(waypoint_vector, position_vector)
        self.result_lbl.text = \
            'Go {}º for {} km'.format(course_vector.heading, course_vector.range)


class WaypointerApp(App):
    def build(self):
        return WaypointerWidget()


if __name__ == '__main__':
    WaypointerApp().run()
