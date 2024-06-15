import flet as ft

class MenuPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Image(src="https://github.com/xorgonix/flet_signal/blob/main/my-app/assets/transparent_circle.png?raw=true", width=150, height=150, fit=ft.ImageFit.CONTAIN),

            ft.Text("Menu", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Explore our delicious menu items:", size=18),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Burger"), subtitle=ft.Text("Juicy beef burger with all the fixings.")),
                    ft.ListTile(title=ft.Text("Fries"), subtitle=ft.Text("Crispy golden fries.")),
                    ft.ListTile(title=ft.Text("Salad"), subtitle=ft.Text("Fresh garden salad.")),
                    ft.ListTile(title=ft.Text("Wings"), subtitle=ft.Text("Spicy buffalo wings.")),
                ]
            )
        ]
