class Cliente:
def __init__(self, nombre: str, correo: str):
    self.nombre = nombre
    self.correo = correo

def validar_email(self) ->bool:
    return "@" in self.correo and  "." in self.correo


client = Cliente("Carla", "correo)