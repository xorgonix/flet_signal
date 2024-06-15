import flet as ft

class HomePage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Image(src="https://github.com/xorgonix/flet_signal/blob/main/my-app/assets/transparent_circle.png?raw=true", width=150, height=150, fit=ft.ImageFit.CONTAIN),
            ft.Text("Welcome to Signal Brewery", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("We are delighted to have you here.", size=24),
            ft.Text("Explore our loyalty program, menu, and specials.", size=18),
        ]
