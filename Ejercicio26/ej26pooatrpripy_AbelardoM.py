class Empleado:
    def __init__(self, nombre: str, sueldo_base: float):
        self.__nombre = None
        self.__sueldo_base = None
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    @property
    def sueldo_base(self) -> float:
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base: float) -> None:
        if not (0 < sueldo_base < 200_000):
            raise ValueError("El sueldo base debe ser mayor que 0 y menor de 200.000 €.")
        self.__sueldo_base = sueldo_base

    def calcular_sueldo(self) -> float:
        return self.sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, comision: float):
        super().__init__(nombre, sueldo_base)
        self.__comision = None
        self.comision = comision

    @property
    def comision(self) -> float:
        return self.__comision

    @comision.setter
    def comision(self, comision: float) -> None:
        if comision >= self.sueldo_base * 0.5:
            raise ValueError("La comisión debe ser menor del 50% del sueldo base.")
        self.__comision = comision

    def calcular_sueldo(self) -> float:
        return self.sueldo_base + self.comision


class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
        super().__init__(nombre, sueldo_base)
        self.__bono_gestion = None
        self.bono_gestion = bono_gestion

    @property
    def bono_gestion(self) -> float:
        return self.__bono_gestion

    @bono_gestion.setter
    def bono_gestion(self, bono: float) -> None:
        if bono >= self.sueldo_base * 0.5:
            raise ValueError("El bono debe ser menor del 50% del sueldo base.")
        self.__bono_gestion = bono

    def calcular_sueldo(self) -> float:
        return self.sueldo_base + self.bono_gestion


empleados = [
    Empleado("Ana", 1200),
    Vendedor("Carlos", 1200, 350),
    Gerente("Marta", 2000, 500),
]

print("--- Sueldos iniciales ---")
for emp in empleados:
    print(f"{emp.nombre} tiene un sueldo de: {emp.calcular_sueldo()} €")

carlos = empleados[1]

print("\n--- Subimos 100 € la comisión de Carlos ---")
carlos.comision += 100
print(f"Nueva comisión: {carlos.comision} € -> sueldo: {carlos.calcular_sueldo()} €")

print("\n--- Intentamos poner un sueldo base negativo ---")
try:
    carlos.sueldo_base = -500
except ValueError as e:
    print(f"Error: {e}")
print(f"El sueldo base de Carlos sigue siendo: {carlos.sueldo_base} €")