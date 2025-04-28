import flet as ft

def add_contract(e):
    print("Add contract")

def add_equipment(e):
    print("Add equipment")

def contracts_view():
    return ft.SafeArea(
        ft.Column(
            [
                ft.Text("Contracts View", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Your contracts will appear here"),
                ft.FilledButton(
                    content=ft.Text("Add New Contract"),
                    on_click=add_contract
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

def equipment_view():
    return ft.SafeArea(
        ft.Column(
            [
                ft.Text("Equipment View", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Your equipment will appear here"),
                ft.FilledButton(
                    content=ft.Text("Add New Equipment"),
                    on_click=add_equipment
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    
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