 from abc import ABC, abstractmethod

 class IRepositorioDB(ABC):
     @abstractmethod
     def guardar (self,pedido):
         pass

 class RepositorioDB(IRepositorioDB):
     def guardar(self, pedido):
      print(f"Guardado pero de forma distinta {pedido} ")

 class ApiTercerosAdapter(IRepositorioDB):
     def guardar(self, pedido)
      print(f"Pedido {pedido} almacenado exitosamente")


 class ServicePedido:
     def __init__(self,repositorio : IRepositorioDB):
         self.repo = repositorio

     def crear_pedido(self, pedido:str):
          print("Notificacion por mensaje")
          print("Impresion de orden")
          self.repo.guardar(pedido)
          print("Notificacion de almacenamiento")

#Dependency injector with pip package
