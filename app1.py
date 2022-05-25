from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = 'Decimal to binary'
            self.input.text = 'Enter a decimal number'
            self.converted.text = ''
            self.label.text = ''
        else:
            self.state = 0
            self.toolbar.title = 'Binary to decimal'
            self.input.text = 'Enter a binary number'
            self.converted.text = ''
            self.label.text = ''

    def convert(self, args):
        if self.state == 0:
            val = int(self.input.text, 2)
            self.converted.text = str(val)
            self.label.text = 'In decimal: '
        else:
            val = format(int(self.input.text), 'b')
            self.converted.text = str(val)
            self.label.text = 'In binary: '

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = 'Teal'
        screen = MDScreen()

        # Toolbar
        self.toolbar = MDToolbar(title='Binary to decimal')
        self.toolbar.pos_hint = {'top': 1}
        self.toolbar.right_action_items = [
            ['rotate-3d-variant', lambda x: self.flip()]
        ]
        screen.add_widget(self.toolbar)

        # Logo
        screen.add_widget(Image(
            source='logo.png',
            pos_hint={'center_x': .5, 'center_y': .7}
        ))

        # Collect user data
        self.input = MDTextField(
            text='Enter a binary number',
            halign='center',
            size_hint=(0.8, 1),
            pos_hint={'center_x': .5, 'center_y': .5},
            font_size=22
        )
        screen.add_widget(self.input)

        # Secondary + primary label
        self.label = MDLabel(
            halign='center',
            pos_hint={'center_x': .5, 'center_y': .35},
            theme_text_color='Secondary'
        )
        screen.add_widget(self.label)

        self.converted = MDLabel(
            halign='center',
            pos_hint={'center_x': .5, 'center_y': .3},
            theme_text_color='Primary',
            font_style='H5'
        )
        screen.add_widget(self.converted)

        # Convert button
        screen.add_widget(MDFillRoundFlatButton(
            text='CONVERT',
            font_size=17,
            pos_hint={'center_x': .5, 'center_y': .15},
            on_press=self.convert
        ))

        return screen


if __name__ == '__main__':
    ConverterApp().run()
