from models.model import Model

class materials(Model):
    __nameTable = 'materials'
    __code_Mmaterial = 'code_Mmaterial'
    __code_class = 'code_class'
    __code_group = 'code_group'
    __name_material = 'name_material'


    def get(self):
        return super().get(self.__nameTable)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def add(self):
        code_Mmaterial = input("Введите code_Mmaterial: ")
        code_class = input("Введите code_class: ")
        code_group = input("Введите code_group: ")
        name_material = input ("Введите name_material: ")
        str = f"{self.__code_Mmaterial}, {self.__code_class}, {self.__code_group}, {self.__name_material}"
        super().add(self.__nameTable, str, code_Mmaterial, code_class, code_group, name_material)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)
