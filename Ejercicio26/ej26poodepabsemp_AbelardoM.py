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

    def quitar_empleado(self, empleado: Empleado) -> None:
        self.empleados.remove(empleado)

    def buscar_empleado(self, nombre: str):
        for emp in self.empleados:
            if emp.nombre == nombre:
                return emp
        return None

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


class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.departamentos = []

    def agregar_departamento(self, departamento: Departamento) -> None:
        self.departamentos.append(departamento)

    def buscar_departamento(self, nombre: str):
        for dep in self.departamentos:
            if dep.nombre == nombre:
                return dep
        return None

    def transferir_empleado(self, nombre_empleado: str, origen: str, destino: str) -> bool:
        dep_origen = self.buscar_departamento(origen)
        dep_destino = self.buscar_departamento(destino)

        if dep_origen is None or dep_destino is None:
            print("Error: departamento de origen o destino no encontrado.")
            return False

        empleado = dep_origen.buscar_empleado(nombre_empleado)
        if empleado is None:
            print(f"Error: {nombre_empleado} no está en el departamento {origen}.")
            return False

        dep_origen.quitar_empleado(empleado)
        dep_destino.agregar_empleado(empleado)
        print(f"{nombre_empleado} transferido de {origen} a {destino}.")
        return True

    def calcular_nomina_global(self) -> float:
        total = 0
        for dep in self.departamentos:
            total += dep.calcular_nomina_total()
        return total

    def mostrar_info_departamentos(self) -> None:
        print(f"##### Empresa {self.nombre} #####")
        print()
        for dep in self.departamentos:
            dep.mostrar_info()


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

empresa = Empresa("Tienda Global")
empresa.agregar_departamento(nacional)
empresa.agregar_departamento(internacional)
empresa.agregar_departamento(nuevos_productos)

print("--- Situación inicial ---")
empresa.mostrar_info_departamentos()
print(f"Nómina global de la empresa: {empresa.calcular_nomina_global()} €")

print("\n--- Transferencia: Carlos de Nacional a Internacional ---")
empresa.transferir_empleado("Carlos", "Nacional", "Internacional")
print()

print("--- Situación final ---")
empresa.mostrar_info_departamentos()
print(f"Nómina global de la empresa: {empresa.calcular_nomina_global()} €")