import flet as ft
from views.contracts_view import contracts_view
from views.equipment_view import equipment_view

    
def add_app_bar(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("ClikTrak"),
        bgcolor=ft.Colors.with_opacity(0.04, ft.CupertinoColors.SYSTEM_BACKGROUND)
    )
    
def add_navigation_bar(page: ft.Page, view_container: ft.Container):
    def change_view(e):
        if e.control.selected_index == 0:
            view_container.content = contracts_view()
        else:
            view_container.content = equipment_view()
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icon(ft.Icons.RECEIPT_LONG_OUTLINED),
                selected_icon=ft.Icon(ft.Icons.RECEIPT_LONG),
                label="Contracts",),
            ft.NavigationBarDestination(
                icon=ft.Icons.CAMERA_ALT_OUTLINED,
                selected_icon=ft.Icons.CAMERA_ALT,
                label="Equipment",),
        ],
        border=ft.Border(
            top=ft.BorderSide(
                color=ft.CupertinoColors.SYSTEM_GREY2,
                width=0,
            )
        ),
        on_change=change_view
    )

def main(page: ft.Page):
    page.adaptive = True
    # Create a container to hold the current view
    view_container = ft.Container(
        content=contracts_view(),
        expand=True
    )
    
    add_app_bar(page)
    add_navigation_bar(page, view_container)
    
    page.add(view_container)
    
ft.app(target=main)