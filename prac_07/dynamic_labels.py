from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Names"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

DynamicLabelsApp().run()
