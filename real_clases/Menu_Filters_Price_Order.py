from abstract_clases.abscract_clases import Menu

class MenuFiltersPrice(Menu):
    def __init__(self, options):
        super().__init__(options)
    # Imprime un numero empezando en 1 hasta n cantidad de elementos que tenga el atributo options
    def display(self):
        for i in range(len(self.options)):
            print(f"{i+1} {self.options[i]}")

    # Retorna un valor que representa la opción selecionada en la lista definida como atributo
    def select(self):
        selected = False
        while not selected:
            user_input = input("¿Cómo quieres ver los precios? (Escribe el número): ")
            if user_input == "1":
                pricesel = "maym"
                selected = True
            if user_input == "2":
                pricesel = "menm"
                selected = True
            if user_input == "3":
                pricesel = "esp"
                selected = True
        return pricesel