import random
# from random import randint (si pongo esto, tengo que borrar el random del random.randint())

class Family:
    def __init__(self, last_name): #init = constructor
        self._last_name = last_name #este es un array, vamos a ir guardando elementos de la familia que crearemos #el _ es privado (es una convencion) se debe modificar por los metodos que se definan
        self._name = ""
        self._age = 0
        self._members = []
    def _generateId(self):
        return random.randint(0, 10) #generador random de numeros

    def add_member(self, member):  #member esta recibiendo un objeto identificado por los []  
        member = {
            "id": self._generateId(),
            "name": member._name,
            "lastname": member._last_name,
            "age": member._age
        }
        self._members.append(member)
        return member

    def delete_member(self, id):
        pass
    def update_member(self, id, member):
        obj = self.get_member(id)
        obj.update(member)
        return obj
    def get_member(self, id):
        member = list(filter(lambda item: item["id"] == id , self._members))
        return member[0]
    def get_all_members(self):
        return self._members



