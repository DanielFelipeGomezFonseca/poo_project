from abstract_clases.abscract_clases import Menu


class MenuMarcas(Menu):
    def __init__(self, options):
        super().__init__(options)

    # Imprime un numero empezando en 1 hasta n cantidad de elementos que tenga el atributo options
    def display(self):
        for i in range(len(self.options)):
            print(f"{i+1} {self.options[i]}")

    # Retorna un valor que representa la opción selecionada en la lista definida como atributo
    def select(self,marcas_list):
        selected = False
        while not selected:
            user_input = input("¿Qué marca deseas ver? (Escribe el número): ")
            for i in range(len(marcas_list)):
                number = str(i+1)
                if user_input == number:
                    marca = marcas_list[i]
                    selected = True
        return marca