from nicegui import ui


######  ui.page("/page_layout") is a decorator that sets the URL of the page to /page_layout ######
@ui.page("/page_layout")

######  def page_layout() is a function that defines the layout of the page  ######
def page_layout():

    ##### Content section of the page #####
    ui.label("CONTENT").style("color: green; font-size: 20px; font-weight: bold")
    [ui.label(f"Line {i}") for i in range(1, 101)]

    ##### Header section of the page #####
    with ui.header(elevated=True).style("background-color: #3874c8").classes(
        "items-center justify-between"
    ):
        ##### button that toggles the left drawer #####
        ui.button(on_click=lambda: left_drawer.toggle(), icon="arrow_back_ios").props(
            "flat color=gray"
        )

        ui.label("HEADER").style("color: red; font-size: 20px; font-weight: bold")

        ##### Toolbar section of the page #####

        ##### button that changes the page title #####
        ui.button(
            "Change page title",
            on_click=lambda: ui.page_title("New title"),
            icon="edit",
        ).props("flat color=orange")

        ##### button that toggles the right drawer #####
        ui.button(on_click=lambda: right_drawer.toggle(), icon="arrow_forward_ios").props("flat color=gray")

    ##### Left drawer section of the page #####
    with ui.left_drawer(top_corner=True, bottom_corner=True).style(
        "background-color: rgb(16, 16, 235)"
    ) as left_drawer:
        ui.label("LEFT DRAWER").style(
            "color: white; font-size: 15px; font-weight: bold"
        )

        ui.separator()

    ##### Right drawer section of the page #####
    with ui.right_drawer(fixed=True).style("background-color: #ebf1fa").props(
        "bordered"
    ) as right_drawer:
        ui.label("RIGHT DRAWER").style(
            "color: black; font-size: 20px; font-weight: bold"
        )

        ui.separator()

    ##### Footer section of the page #####
    with ui.footer().style("background-color: #7fef79"):
        ui.label("FOOTER").style(
            "color: rgb(255, 0, 0); font-size: 20px; font-weight: bold"
        )


######  ui.link("show page with fancy layout", page_layout) is a link that opens the page_layout function ######
ui.link("show page with fancy layout", page_layout)

ui.run(title="Page Layout")
