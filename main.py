import flet as ft
from math import sqrt, sin, cos, tan, log, pi, e

# Function to handle button presses
def button_press(value, input_display, page):
    current = input_display.value
    if value == "C":
        input_display.value = ""
    elif value == "=":
        try:
            # Replace '÷' with '/' and '×' with '*' for evaluation
            expression = current.replace("÷", "/").replace("×", "*")
            result = eval(expression)
            input_display.value = str(result)
        except Exception:
            input_display.value = "Error"
    elif value == "√":
        try:
            result = sqrt(float(current))
            input_display.value = str(result)
        except Exception:
            input_display.value = "Error"
    elif value == "^":
        input_display.value += "**"
    elif value == "π":
        input_display.value += str(pi)
    elif value == "e":
        input_display.value += str(e)
    else:
        input_display.value += value
    page.update()

# Main application
def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Input display
    input_display = ft.TextField(
        value="",
        text_align=ft.TextAlign.RIGHT,
        width=300,
        read_only=True,
        border_color=ft.colors.TRANSPARENT,
        border_width=0,
        autofocus=True,
    )

    # Buttons for the calculator
    buttons = [
        ("C", "#ff6666"), ("√", "#ffcc66"), ("^", "#ffcc66"), ("÷", "#ffcc66"),
        ("7", "#666"), ("8", "#666"), ("9", "#666"), ("×", "#ffcc66"),
        ("4", "#666"), ("5", "#666"), ("6", "#666"), ("-", "#ffcc66"),
        ("1", "#666"), ("2", "#666"), ("3", "#666"), ("+", "#ffcc66"),
        ("0", "#666"), (".", "#666"), ("=", "#66cc66"), ("π", "#666"),
        ("sin", "#666"), ("cos", "#666"), ("tan", "#666"), ("log", "#666"),
        ("e", "#666"), ("(", "#666"), (")", "#666"), ("", "#333"),
    ]

    # Create buttons layout
    grid = ft.GridView(
        expand=True,
        runs_count=4,
        spacing=5,
        run_spacing=5,
        child_aspect_ratio=1,
    )

    for text, color in buttons:
        if text:
            btn = ft.ElevatedButton(
                text=text,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=color,
                ),
                width=50,
                height=50,
                on_click=lambda e, t=text: button_press(t, input_display, page),
            )
            grid.controls.append(btn)

    # Add components to the page
    page.add(
        ft.Column(
            [
                input_display,
                grid,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

# Run the app
if __name__ == "__main__":
    ft.app(target=main)
