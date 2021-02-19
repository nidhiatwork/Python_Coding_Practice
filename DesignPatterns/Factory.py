class Button:
    html = ""
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
    def create_button(self, type):
        t = type.capitalize()
        return globals()[t]()

b = ButtonFactory()
types = ["image", "input", "flash"]
for type in types:
    print(b.create_button(type).get_html())