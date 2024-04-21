"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import pytesseract as pt
from PIL import Image
import reflex as rx
import components.downloadHandler as dh

filename:str = f"{config.app_name}/{config.app_name}.py"




def index() -> rx.Component:
    return dh.Downloads()


app:rx.App = rx.App(
    theme= rx.theme(
            appearance="dark",
            accent_color="ruby",
            gray_color="sand", 
            radius="full"
        ),
    )
app.add_page(index)