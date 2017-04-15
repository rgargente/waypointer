import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from vector import Vector

kivy.require('1.9.1')  # replace with your current kivy version !


class WaypointerWidget(BoxLayout):
    result_lbl = ObjectProperty(None)
    waypoint_vector = ObjectProperty(None)
    position_vector = ObjectProperty(None)
    guideme_btn = ObjectProperty(None)

    def set_guideme_state(self):
        self.guideme_btn.disabled = not (self.waypoint_vector.heading
                                         and self.waypoint_vector.range
                                         and self.position_vector.heading
                                         and self.position_vector.range)

    def on_guideme_press(self):
        waypoint_vector = Vector(float(self.waypoint_vector.heading), float(self.waypoint_vector.range))
        position_vector = Vector(float(self.position_vector.heading), float(self.position_vector.range))
        course_vector = Vector.get_course(waypoint_vector, position_vector)
        self.result_lbl.text = \
            'Head {:.0f}º for {:.2f} km'.format(course_vector.heading, course_vector.range)


class ValidatedTextInput(TextInput):
    def on_focus(self, obj, focused):
        if not focused:
            self.dispatch('on_text_validate')


class HeadingTextInput(ValidatedTextInput):
    heading = BoundedNumericProperty(0, min=0, max=359, errorvalue=359)

    def on_text_validate(self):
        if self.text:
            self.heading = float(self.text)
            self.text = str(self.heading)


class RangeTextInput(ValidatedTextInput):
    range = NumericProperty(0, min=0)

    def on_text_validate(self):
        if self.text:
            self.range = float(self.text)
            self.text = str(self.range)


class WaypointerApp(App):
    def build(self):
        return WaypointerWidget()


if __name__ == '__main__':
    WaypointerApp().run()
