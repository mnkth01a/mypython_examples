from nicegui import ui

columns = [
    {"name": "name", "label": "Product", "field": "name", "align": "center"},
    {"name": "sales", "label": "Sales", "field": "sales", "align": "center"},
]
rows = [
    {"name": "A", "data": [10, 8, 2, 4, 5, 6, 7, 8, 9, 10]},
    {"name": "B", "data": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14]},
    {"name": "C", "data": [2, 1, 3, 7, 8, 9, 10, 11, 12, 13]},
]
table = ui.table(columns=columns, rows=rows, row_key="name").classes("w-100")
for r, row in enumerate(rows):
    with ui.teleport(f"#c{table.id} tr:nth-child({r+1}) td:nth-child(2)"):
        ui.echart(
            {
                "xAxis": {"type": "category", "show": True},
                "yAxis": {"type": "value", "show": True},
                "series": [{"type": "line", "data": row["data"]}],
            }
        ).classes("w-80 h-25")

ui.run()
