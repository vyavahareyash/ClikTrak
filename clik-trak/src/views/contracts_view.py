import flet as ft

def add_contract(e):
    print("Add contract")

def add_contract_row(contract_name, amount):
    return ft.DataRow(
        cells=[
            ft.DataCell(ft.Text("Contract Name")),
            ft.DataCell(ft.Text("$5,000")),
        ]
    )   

def create_contracts_table():
    return ft.Container(
        content=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Contract Name")),
                ft.DataColumn(ft.Text("Amount"), numeric=True),
            ],
            rows=[
                add_contract_row("Website Development", "$5,000"),
                add_contract_row("Mobile App Development", "$8,500"),
                add_contract_row("UI/UX Design", "$3,200"),
                add_contract_row("Content Management", "$2,800"),
            ],
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_300),
            horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREY_300),
        ),
        padding=20,
    )

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
                            create_contracts_table(),
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