from abstract_clases.abscract_clases import Menu


class MenuPages(Menu):
    def __init__(self, options):
        super().__init__(options)
    def display(self):
        for i in range(len(self.options)):
            print(f"{i+1} {self.options[i]}")
    def select(self):
        selected = False
        while not selected:
            user_input = input("¿En que página deseas buscar? (Escribe el número): ")
            if user_input == "1":
                page = "Panamericana"
                selected = True
            if user_input == "2":
                page = "Fallabela"
                selected = True
            if user_input == "3":
                page = "Alkosto"
                selected = True
        return page