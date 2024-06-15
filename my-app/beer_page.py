import flet as ft

class BeerPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Image(src="https://github.com/xorgonix/flet_signal/blob/main/my-app/assets/transparent_circle.png?raw=true", width=150, height=150, fit=ft.ImageFit.CONTAIN),

            ft.Text("Our Beers", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Discover our variety of craft beers:", size=18),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Pale Ale"), subtitle=ft.Text("A crisp and refreshing pale ale.")),
                    ft.ListTile(title=ft.Text("Stout"), subtitle=ft.Text("A rich and creamy stout.")),
                    ft.ListTile(title=ft.Text("IPA"), subtitle=ft.Text("A hoppy and bitter IPA.")),
                    ft.ListTile(title=ft.Text("Lager"), subtitle=ft.Text("A smooth and easy-drinking lager.")),
                ]
            )
        ]
