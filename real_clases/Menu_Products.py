from abstract_clases.abscract_clases import Menu

class MenuProducts(Menu):
    def __init__(self, options):
        super().__init__(options)
    def display(self):
        for i in range(len(self.options)):
            print(f"{i+1} {self.options[i]}")
    def select(self):
        selected = False
        while not selected:
            user_input = input("¿Que productos deseas buscar? (Escribe el número): ")
            if user_input == "1":
                prod = "audifonos"
                selected = True
            if user_input == "2":
                prod = "mouse"
                selected = True
            if user_input == "3":
                prod = "teclado"
                selected = True
        return prod
