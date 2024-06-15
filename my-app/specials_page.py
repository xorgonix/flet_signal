import flet as ft

class SpecialsPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Image(src="https://github.com/xorgonix/flet_signal/blob/main/my-app/assets/transparent_circle.png?raw=true", width=150, height=150, fit=ft.ImageFit.CONTAIN),
            ft.Text("Specials", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Check out our current specials:", size=18),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Happy Hour"), subtitle=ft.Text("50% off all drinks from 4-6 PM.")),
                    ft.ListTile(title=ft.Text("Taco Tuesday"), subtitle=ft.Text("2-for-1 tacos all day.")),
                    ft.ListTile(title=ft.Text("Wing Wednesday"), subtitle=ft.Text("Half-price wings from 6-9 PM.")),
                    ft.ListTile(title=ft.Text("Sunday Brunch"), subtitle=ft.Text("Special brunch menu from 10 AM-2 PM.")),
                ]
            )
        ]
