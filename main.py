import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_light
from dearpygui_ext.themes import create_theme_imgui_dark

def switch_theme_callback(sender, app_data, user_data):
    switch_theme(user_data)

def switch_theme(theme):
    global light_theme
    global dark_theme
    if theme == "dark":
        dpg.bind_theme(dark_theme)
    elif theme == "light":
        dpg.bind_theme(light_theme)
    else:
        print("Theme", theme, "is not supported!")


def print_me(sender):
    print(f"Menu Item: {sender}")

def quit_app(sender):
    dpg.stop_dearpygui()

dpg.create_context()

# We need to get the themes here otherwise the context will not be created yet...
light_theme = create_theme_imgui_light()
dark_theme = create_theme_imgui_dark()

# Add Fira Code as main font
with dpg.font_registry():
    default_font = dpg.add_font("./res/fonts/fira_code/FiraCode-Regular.ttf", 20)
    dpg.bind_font(default_font)

with dpg.window(tag="Primary Window"):
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save", callback=print_me)
            dpg.add_menu_item(label="Save As", callback=print_me)

        with dpg.menu(label="Theme"):
            dpg.add_menu_item(label="Set Light Theme", callback=switch_theme_callback, user_data="light")
            dpg.add_menu_item(label="Set Dark Theme", callback=switch_theme_callback, user_data="dark")
        dpg.add_menu_item(label="About", callback=print_me)
        dpg.add_menu_item(label="Quit", callback=quit_app)


dpg.create_viewport(title='PyEdit')

switch_theme("light")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()