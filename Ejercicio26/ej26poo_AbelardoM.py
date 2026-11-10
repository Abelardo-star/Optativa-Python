class Empleado:
    def __init__(self, nombre: str, sueldo_base: float):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self) -> float:
        return self.sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, comision: float):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self) -> float:
        return self.sueldo_base + self.comision


class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion

    def calcular_sueldo(self) -> float:
        return self.sueldo_base + self.bono_gestion


empleados = [
    Empleado("Ana", 1200),
    Vendedor("Carlos", 1200, 350),
    Gerente("Marta", 2000, 500)
]

for emp in empleados:
    print(f"{emp.nombre} tiene un sueldo de: {emp.calcular_sueldo()} €")