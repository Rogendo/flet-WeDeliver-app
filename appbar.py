import flet 
from flet import *
from flet import colors
#appbar 
jumbotron = AppBar(
    toolbar_height=90,
    bgcolor="#E3002A",
    title=Row([
        Container(
            padding=padding.all(3),
            border=border.all(2, "white"),
            border_radius=border_radius.all(30),
            content=Text("Location",color="white",size=13)

        ),
        Container(
            content=Image(
                src="assets/images/logo.png",
                width=100,
                height=70,
            )
        )
    ],alignment="spaceBetween"

    )

)
