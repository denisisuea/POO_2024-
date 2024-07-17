# SEMANA 3
class ClimaDiario:
    def __init__(self):
        """
        Constructor que inicializa una lista vacía para almacenar las temperaturas diarias.
        """
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        """
        Método para agregar una temperatura a la lista.
        """
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de las temperaturas.
        """
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

def main():
    """
    Función principal para coordinar la entrada y el cálculo del promedio usando POO.
    """
    clima_semanal = ClimaDiario()

    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        clima_semanal.ingresar_temperatura(temp)

    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()