# SEMANA 6
'''Ejemplo de Sistema de Gestión de Empleados'''

# Definición de la clase base Empleado
class Empleado: # Clase Empleado
    def __init__(self, nombre, salario): # Inicializa los atributos, nombre y salario
        self.nombre = nombre
        self._salario = salario  # Atributo protegido (encapsulación)

    def descripcion(self): # Método descripción (Para obtener el salario)
        return f"{self.nombre} tiene un salario de {self._salario}"

    def calcular_pago(self): # Métodod calcular_pago
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

# Clase derivada EmpleadoTiempoCompleto que hereda de Empleado
class EmpleadoTiempoCompleto(Empleado): # Clase EmpleadoTiempoCompleto
    def __init__(self, nombre, salario, beneficios):
        super().__init__(nombre, salario) # Herencia de la clase Empleado
        self.__beneficios = beneficios  # Atributo privado (encapsulación)

    # Método sobrescrito de la clase base (polimorfismo)
    def calcular_pago(self):
        return self._salario

    # Método público para obtener los beneficios (encapsulación)
    def get_beneficios(self):
        return self.__beneficios

# Clase derivada EmpleadoPorHoras que hereda de Empleado
class EmpleadoPorHoras(Empleado): # Clase EmpleadoPorHoras
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, salario_por_hora)
        self.horas_trabajadas = horas_trabajadas

    # Método sobrescrito de la clase base (polimorfismo)
    def calcular_pago(self): # Método calcular_pago
        return self._salario * self.horas_trabajadas # Calculo del pago por horas trabajadas

# Creación de instancias de las clases
empleado_tiempo_completo = EmpleadoTiempoCompleto("Jefferson", 3000, "Seguro médico")
empleado_por_horas = EmpleadoPorHoras("Brigitte", 20, 120)

# Uso de métodos y demostración de polimorfismo
print(empleado_tiempo_completo.descripcion())  # Salida: Jefferson tiene un salario de 3000
print("Pago mensual:", empleado_tiempo_completo.calcular_pago())  # Salida: Pago mensual: 3000
print("Beneficios:", empleado_tiempo_completo.get_beneficios())  # Salida: Beneficios: Seguro médico

print(empleado_por_horas.descripcion())  # Salida: Brigitte tiene un salario de 20
print("Pago mensual:", empleado_por_horas.calcular_pago())  # Salida: Pago mensual: 2400
print("Horas trabajadas:", empleado_por_horas.horas_trabajadas)  # Salida: Horas trabajadas: 120