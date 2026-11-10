class Empleado:
    def __init__(self, nombre: str, sueldo_base: float):
        self.__nombre = None
        self.__sueldo_base = None
        self.set_nombre(nombre)
        self.set_sueldo_base(sueldo_base)

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    def get_sueldo_base(self) -> float:
        return self.__sueldo_base

    def set_sueldo_base(self, sueldo_base: float) -> None:
        if not (0 < sueldo_base < 200_000):
            raise ValueError("El sueldo base debe ser mayor que 0 y menor de 200.000 €.")
        self.__sueldo_base = sueldo_base

    def calcular_sueldo(self) -> float:
        return self.get_sueldo_base()


class Vendedor(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, comision: float):
        super().__init__(nombre, sueldo_base)
        self.__comision = None
        self.set_comision(comision)

    def get_comision(self) -> float:
        return self.__comision

    def set_comision(self, comision: float) -> None:
        if comision >= self.get_sueldo_base() * 0.5:
            raise ValueError("La comisión debe ser menor del 50% del sueldo base.")
        self.__comision = comision

    def calcular_sueldo(self) -> float:
        return self.get_sueldo_base() + self.get_comision()


class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
        super().__init__(nombre, sueldo_base)
        self.__bono_gestion = None
        self.set_bono_gestion(bono_gestion)

    def get_bono_gestion(self) -> float:
        return self.__bono_gestion

    def set_bono_gestion(self, bono: float) -> None:
        if bono >= self.get_sueldo_base() * 0.5:
            raise ValueError("El bono debe ser menor del 50% del sueldo base.")
        self.__bono_gestion = bono

    def calcular_sueldo(self) -> float:
        return self.get_sueldo_base() + self.get_bono_gestion()


empleados = [
    Empleado("Ana", 1200),
    Vendedor("Carlos", 1200, 350),
    Gerente("Marta", 2000, 500),
]

print("--- Sueldos iniciales ---")
for emp in empleados:
    print(f"{emp.get_nombre()} tiene un sueldo de: {emp.calcular_sueldo()} €")

carlos = empleados[1]

print("\n--- Subimos 100 € la comisión de Carlos ---")
carlos.set_comision(carlos.get_comision() + 100)
print(f"Nueva comisión: {carlos.get_comision()} € -> sueldo: {carlos.calcular_sueldo()} €")

print("\n--- Intentamos poner un sueldo base negativo ---")
try:
    carlos.set_sueldo_base(-500)
except ValueError as e:
    print(f"Error: {e}")
print(f"El sueldo base de Carlos sigue siendo: {carlos.get_sueldo_base()} €")