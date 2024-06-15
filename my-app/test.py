import flet as ft
import os

def main(page: ft.Page):
    page.title = "Image Test"
    
    # Log the current working directory and the image path
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    image_path = "/assets/transparent_circle.png"
    full_image_path = os.path.join(cwd, "assets", "transparent_circle.png")
    print(f"Image path: {image_path}")
    print(f"Full image path: {full_image_path}")
    
    # Check if the image file exists
    if os.path.exists(full_image_path):
        print("Image file exists.")
    else:
        print("Image file does not exist.")
    
    page.add(ft.Image(src=image_path, width=150, height=150, fit=ft.ImageFit.CONTAIN))
    page.update()

ft.app(target=main, assets_dir="assets")
