from dataclasses import dataclass
@dataclass
class Persona:
    nombre: str
#dataclass

@dataclass
class PersonaDto(Persona):
    edad : int
    cat: str

person = PersonaDto("Alexa",25, "Dev")

print(person)