from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

def callback(instance):
		print("Button <%s> pressed" % instance.text)

class Connect4(App):
	def build(self):
		layout = BoxLayout(spacing=10, orientation="vertical")

		welcome_message = Label(text="Please choose Connect4 mode")

		btn1 = Button(text="CPU vs. CPU")
		btn1.bind(on_press=callback)
		btn2 = Button(text="Human vs. CPU")
		btn2.bind(on_press=callback)
		btn3 = Button(text="Human vs. Human")
		btn3.bind(on_press=callback)

		layout.add_widget(welcome_message)
		layout.add_widget(btn1)
		layout.add_widget(btn2)
		layout.add_widget(btn3)

		return layout

if __name__ == "__main__":
	Connect4().run()