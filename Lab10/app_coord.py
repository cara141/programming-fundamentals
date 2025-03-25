from ui.ui import ConsoleUI

version = input("""
    Alegeti modul de functionare:
    1. fisier
    2. memorie
    """)
while True:
    match version:
        case "1":
            ui = ConsoleUI("file")
            ui.run()
        case "2":
            ui = ConsoleUI("memory")
            ui.run()
        case _:
            print("Input invalid!")

