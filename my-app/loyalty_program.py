import flet as ft

class LoyaltyProgramPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Image(src="https://github.com/xorgonix/flet_signal/blob/main/my-app/assets/transparent_circle.png?raw=true", width=150, height=150, fit=ft.ImageFit.CONTAIN),
            ft.Text("Welcome to Signal Brewery Loyalty Program", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Earn points for every purchase and get exclusive rewards!", size=18),
            ft.Divider(),
            ft.Row(
                controls=[
                    ft.Text("Points Earned: ", size=16),
                    ft.Text("150", size=16, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Text("Rewards Available: ", size=16),
                    ft.Text("5", size=16, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.ElevatedButton(text="Redeem Rewards", on_click=self.redeem_rewards)
        ]

    def redeem_rewards(self, e):
        dialog = ft.AlertDialog(
            title=ft.Text("Redeem Rewards"),
            content=ft.Text("This feature is coming soon! Stay tuned."),
            actions=[
                ft.TextButton("Close", on_click=self.close_dialog)
            ]
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def close_dialog(self, e):
        self.page.dialog.open = False
        self.page.update()
