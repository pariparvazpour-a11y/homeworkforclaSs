!pip install kivy -i https://pypi.tuna.tsinghua.edu.cn/simple


import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class Gallery(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.image_folder = "images"
        self.images = [
            os.path.join(self.image_folder, f)
            for f in os.listdir(self.image_folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]

        self.index = 0

        # نمایش تصویر 
        self.img = Image(source=self.images[self.index])
        self.add_widget(self.img)

        #  دکمه 
        self.btn = Button(
            text="عکس بعدی",
            size_hint=(1, 0.2)
        )
        self.btn.bind(on_press=self.next_image)
        self.add_widget(self.btn)

    def next_image(self, instance):
        self.index = (self.index + 1) % len(self.images)
        self.img.source = self.images[self.index]
        self.img.reload()


class GalleryApp(App):
    def build(self):
        return Gallery()


if __name__ == "__main__":
    GalleryApp().run()
