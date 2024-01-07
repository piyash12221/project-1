from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math

Window.size = (450, 844)


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "sqrt", "^2"]
        self.title = "Piyash_Calculator"
        self.last_was_operator = None
        self.last_button = None
        self.icon = "Calculator.png"

        main_layout = BoxLayout(orientation="vertical", spacing=-2)
        self.solution = TextInput(
            background_color="#D3D3D3",
            foreground_color="black",
            multiline=True,
            halign="right",
            font_size=50,
            readonly=True,
            height=70,
        )

        main_layout.add_widget(self.solution)

        # Create a horizontal layout for square root and square buttons
        root_square_layout = BoxLayout(spacing=-2)

        sqrt_button = Button(
            text="√", font_size=30, background_color="#1F51FF",
            pos_hint={"center_x": 0.25, "center_y": 0.50},
            padding=[0, 0, 0, 0], bold="true"
        )
        sqrt_button.bind(on_press=self.on_square_root)
        root_square_layout.add_widget(sqrt_button)

        square_button = Button(
            text="^2", font_size=30, background_color="#1F51FF",
            pos_hint={"center_x": 0.75, "center_y": 0.50},
            padding=[0, 0, 0, 0], bold="true"
        )
        square_button.bind(on_press=self.on_square)
        root_square_layout.add_widget(square_button)

        main_layout.add_widget(root_square_layout)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            ["C", "0", ".", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=-2)
            for label in row:
                if label in self.operators:
                    button_color = "#1F51FF"
                else:
                    button_color = "#36454F"

                button = Button(
                    text=label, font_size=30, background_color=button_color,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}, bold="true"
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=30, background_color="#71797E",
            pos_hint={"center_x": 0.5, "center_y": 0.5}, bold="true"
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

    def on_square_root(self, instance):
        current = self.solution.text
        if current and current[0] != "-":
            # Ensure the number is non-negative before taking the square root
            result = math.sqrt(float(current))
            self.solution.text = str(result)

    def on_square(self, instance):
        current = self.solution.text
        if current:
            result = str(float(current) ** 2)
            self.solution.text = result


if __name__ == "__main__":
    MainApp().run()
