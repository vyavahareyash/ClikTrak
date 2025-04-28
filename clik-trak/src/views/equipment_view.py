import flet as ft

def add_equipment(e):
    print("Add equipment")

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