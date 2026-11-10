from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre: str, sueldo_base: float):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    @abstractmethod
    def calcular_sueldo(self) -> float:
        pass


class EmpleadoBase(Empleado):
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


class Departamento:
    def __init__(self, nombre: str, gerente: Gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def agregar_empleado(self, empleado: Empleado) -> None:
        self.empleados.append(empleado)

    def calcular_nomina_total(self) -> float:
        total = self.gerente.calcular_sueldo()
        for emp in self.empleados:
            total += emp.calcular_sueldo()
        return total

    def mostrar_info(self) -> None:
        print(f"=== Departamento {self.nombre} ===")
        print(f"Gerente: {self.gerente.nombre} - sueldo: {self.gerente.calcular_sueldo()} €")
        print("Empleados:")
        for emp in self.empleados:
            tipo = type(emp).__name__
            print(f"  - {emp.nombre} ({tipo}) - sueldo: {emp.calcular_sueldo()} €")
        print(f"Nómina total del departamento: {self.calcular_nomina_total()} €")
        print()


ana = EmpleadoBase("Ana", 1200)
carlos = Vendedor("Carlos", 1200, 350)
marta = Gerente("Marta", 2000, 450)

nacional = Departamento("Nacional", marta)
nacional.agregar_empleado(ana)
nacional.agregar_empleado(carlos)

john = Gerente("John", 2500, 850)
internacional = Departamento("Internacional", john)
internacional.agregar_empleado(Vendedor("Sarah", 1500, 600))
internacional.agregar_empleado(Vendedor("Pierre", 1500, 550))

nuevos_productos = Departamento("Nuevos Productos", marta)
nuevos_productos.agregar_empleado(EmpleadoBase("Jaime", 1200))
nuevos_productos.agregar_empleado(Vendedor("Secundino", 1200, 350))

departamentos = [nacional, internacional, nuevos_productos]

for dep in departamentos:
    dep.mostrar_info()