import flet as ft

def main(page: ft.Page):

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

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