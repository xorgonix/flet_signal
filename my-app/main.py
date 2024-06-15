import flet as ft
from home_page import HomePage
from loyalty_program import LoyaltyProgramPage
from beer_page import BeerPage
from menu_page import MenuPage
from specials_page import SpecialsPage

def main(page: ft.Page):
    page.title = "Signal Brewery Loyalty Program"
    page.adaptive = True

    def navigate(e):
        page.views.clear()
        if e.control.selected_index == 0:
            page.views.append(ft.View(controls=[HomePage(page)], appbar=appbar, navigation_bar=navigation_bar))
        elif e.control.selected_index == 1:
            page.views.append(ft.View(controls=[LoyaltyProgramPage(page)], appbar=appbar, navigation_bar=navigation_bar))
        elif e.control.selected_index == 2:
            page.views.append(ft.View(controls=[BeerPage(page)], appbar=appbar, navigation_bar=navigation_bar))
        elif e.control.selected_index == 3:
            page.views.append(ft.View(controls=[MenuPage(page)], appbar=appbar, navigation_bar=navigation_bar))
        elif e.control.selected_index == 4:
            page.views.append(ft.View(controls=[SpecialsPage(page)], appbar=appbar, navigation_bar=navigation_bar))
        page.update()

    appbar = ft.AppBar(
        leading=ft.TextButton("Home", style=ft.ButtonStyle(padding=0)),
        title=ft.Text("Signal Brewery"),
        actions=[
            ft.IconButton(ft.icons.ADD, style=ft.ButtonStyle(padding=0))
        ],
        bgcolor=ft.colors.with_opacity(0.04, ft.colors.BLACK),
    )

    navigation_bar = ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Loyalty"),
            ft.NavigationDestination(icon=ft.icons.LOCAL_DRINK, label="Beer"),
            ft.NavigationDestination(icon=ft.icons.RESTAURANT_MENU, label="Menu"),
            ft.NavigationDestination(icon=ft.icons.LOCAL_OFFER, label="Specials"),
        ],
        on_change=navigate,
        border=ft.Border(
            top=ft.BorderSide(color=ft.colors.GREY, width=0)
        ),
    )

    page.views.append(ft.View(controls=[HomePage(page)], appbar=appbar, navigation_bar=navigation_bar))
    page.update()

ft.app(target=main, assets_dir="assets")
