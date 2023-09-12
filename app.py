import flet
from flet import *
from appbar import jumbotron

def main(page:Page):
  page.title=("We.Deliver")
  page.padding=0
  page.spacing=0

  page.add(

  #appbar
  jumbotron,

  #navigation bar

  

  )

flet.app(target=main, assets_dir="assets")
