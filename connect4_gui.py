from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class ModeScreen(Screen):
	def __init__(self, **kwargs):
		super(ModeScreen, self).__init__(** kwargs)

		mode_layout = BoxLayout(spacing=10, orientation="vertical")

		welcome_message = Label(text="Please choose Connect4 mode")

		btn1 = Button(text="CPU vs. CPU")
		btn1.bind(on_press=self.mode_select)
		btn2 = Button(text="Human vs. CPU")
		btn2.bind(on_press=self.mode_select)
		btn3 = Button(text="Human vs. Human")
		btn3.bind(on_press=self.mode_select)

		mode_layout.add_widget(welcome_message)
		mode_layout.add_widget(btn1)
		mode_layout.add_widget(btn2)
		mode_layout.add_widget(btn3)

		self.add_widget(mode_layout)

	def mode_select(self, *args):
		self.manager.current = "game"


class GameScreen(Screen):
	def __init__(self, **kwargs):
		super(GameScreen, self).__init__(**kwargs)

		game_layout = GridLayout(cols=7, rows=7)

		for i in range(6):
			for j in range(7):
				game_layout.add_widget(Button(text=str(i) + ", " + str(j)))

		for i in range(7):
			game_layout.add_widget(Button(text="Pick column " + str(i)))

		self.add_widget(game_layout)


class Connect4GUI(App):

	def build(self):

		# adding screens to the screen manager
		screen_manager = ScreenManager()
		mode_screen = ModeScreen(name="mode")
		game_screen = GameScreen(name="game")
		screen_manager.add_widget(mode_screen)
		screen_manager.add_widget(game_screen)
		return screen_manager


if __name__ == "__main__":
	Connect4GUI().run()