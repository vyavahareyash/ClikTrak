import flet as ft

def add_contract(e):
    print("Add contract")

def add_equipment(e):
    print("Add equipment")

def contracts_view():
    return ft.SafeArea(
        ft.Stack(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Text("Contracts", size=20, weight=ft.FontWeight.BOLD),
                                alignment=ft.alignment.center,
                                padding=20
                            ),
                            ft.Container(
                                content=ft.DataTable(
                                    columns=[
                                        ft.DataColumn(ft.Text("Contract Name")),
                                        ft.DataColumn(ft.Text("Amount"), numeric=True),
                                    ],
                                    rows=[
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Website Development")),
                                                ft.DataCell(ft.Text("$5,000")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Mobile App Development")),
                                                ft.DataCell(ft.Text("$8,500")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("UI/UX Design")),
                                                ft.DataCell(ft.Text("$3,200")),
                                            ]
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Content Management")),
                                                ft.DataCell(ft.Text("$2,800")),
                                            ]
                                        ),
                                    ],
                                    border=ft.border.all(1, ft.Colors.GREY_300),
                                    border_radius=10,
                                    vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_300),
                                    horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREY_300),
                                ),
                                padding=20,
                            ),
                        ],
                        expand=True,
                        spacing=0,
                    ),
                    alignment=ft.alignment.top_center,
                    expand=True
                ),
                ft.Container(
                    content=ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=add_contract,
                        bgcolor=ft.Colors.BLUE,
                        shape=ft.CircleBorder(),
                    ),
                    alignment=ft.alignment.bottom_right,
                    padding=20,
                )
            ],
            expand=True
        )
    )

def equipment_view():
    return ft.SafeArea(
        ft.Stack(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Equipment View", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text("Your equipment will appear here"),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ),
                ft.Container(
                    content=ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=add_equipment,
                        bgcolor=ft.Colors.BLUE,
                        shape=ft.CircleBorder(),
                    ),
                    alignment=ft.alignment.bottom_right,
                    padding=20,
                )
            ],
            expand=True
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