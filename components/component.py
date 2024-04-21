import reflex as rx


def format(article) -> rx.Component:
  return rx.center(
    rx.text(article.nombre),
    rx.text(article.id),
    rx.text(article.fecha)
  )
  

def Articles(articles) -> rx.Component:
  return rx.foreach(articles, format)