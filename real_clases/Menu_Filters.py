from abstract_clases.abscract_clases import Menu

class MenuFilters(Menu):
    def __init__(self, options):
        super().__init__(options)
    def display(self):
        for i in range(len(self.options)):
            print(f"{i+1} {self.options[i]}")
    def select(self):
        selected = False
        while not selected:
            user_input = input("¿Cómo quieres revisar la información? (Escribe el número): ")
            if user_input == "1":
                selection = "todo"
                selected = True
            if user_input == "2":
                selection = "filtrado"
                selected = True
        return selection