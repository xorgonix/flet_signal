import flet as ft

def main(page: ft.Page):
    page.title = "To-Do List"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    tasks = []

    def add_task(e):
        task_name = task_input.value.strip()
        if task_name:
            task = ft.Row(
                [
                    ft.Checkbox(label=task_name, on_change=update_task_status),
                    ft.IconButton(ft.icons.DELETE, on_click=remove_task, data=task_name)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
            tasks.append(task)
            task_input.value = ""
            update_task_list()

    def update_task_list():
        task_list.controls.clear()
        task_list.controls.extend(tasks)
        page.update()

    def update_task_status(e):
        checkbox = e.control
        checkbox.label = f"[DONE] {checkbox.label}" if checkbox.value else checkbox.label[7:]
        page.update()

    def remove_task(e):
        task_name = e.control.data
        task_to_remove = next(task for task in tasks if task.controls[1].data == task_name)
        tasks.remove(task_to_remove)
        update_task_list()

    task_input = ft.TextField(hint_text="Add a new task", on_submit=add_task)
    task_list = ft.Column()

    page.add(
        ft.Column(
            [
                ft.Text("My To-Do List", size=24, weight=ft.FontWeight.BOLD),
                task_input,
                task_list,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

ft.app(target=main, port=8080)
