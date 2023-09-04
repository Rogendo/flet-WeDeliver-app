import flet as ft

def main(page: ft.Page):

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.DELIVERY_DINING,size=60),
        leading_width=60,
        title=ft.Text("We Deliver", style=ft.TextStyle(size=20)),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            # ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.NOTIFICATIONS),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Settings"),
                    ft.PopupMenuItem(text="Send Feedback"),

                    ft.PopupMenuItem(text="About"),
                    ft.PopupMenuItem(text="Terms of Use"),

                    ft.PopupMenuItem(text="Privacy Policy"),


                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.add(
    ft.Row(
        [
            ft.Container(
                content=ft.Text("Non clickable"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER,
                width=150,
                height=150,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Text("Clickable without Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREEN_200,
                width=150,
                height=150,
                border_radius=10,
                on_click=lambda e: print("Clickable without Ink clicked!"),
            ),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ),
)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.CHAT_BUBBLE, label="Inbox"),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
                selected_icon=ft.icons.ACCOUNT_CIRCLE,
                label="Account",
            ),
        ]
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)