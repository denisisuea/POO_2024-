# SEMANA 3 
def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias de la semana.
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio semanal de las temperaturas.
    """
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

def main():
    """
    Función principal para coordinar la entrada y el cálculo del promedio.
    """
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()