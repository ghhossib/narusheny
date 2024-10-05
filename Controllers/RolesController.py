#В данном классе созданы методы для работы с атрибутами класса Roles
from Models.Roles import *
class RolesControllers(Roles):
    #Инициализация атрибутов класса
    def init(self,role):
        super().init(role)

    #Список ролей
    roles = []
    #Методы CRUD
    #создание роли
    def add(self):
        self.roles.append({"role" : self.role})

    #Метод вывода
    @property
    def get(self):
        for element in self.roles:
            print("Роль :", element["role"])

    #Вывести одну роль по его индексу
    def show(self,index):
        if index < len(self.roles):
            print("Роль : ", self.roles[index]["role"])
        else:
            print(f"Роли с индексом {index} не существует")

    #Изменить
    @get.setter
    def get(self, new_role):
        self.role = new_role

    #Метод изменения значения словаря по индексу в списке

    def update(self, index, new_role):
        if index < len(self.roles):
            self.roles[index]["role"] = new_role
            print("Название роли изменено")
        else:
            print(f"Роли с индексом {index} не существует")

    #Удалить из спска
    def delete(self, index):
        if index < len(self.roles):
            name_role = self.roles[index]['role']
            self.roles.pop(index)
            print(f"Запись {name_role} удалена")
        else:
            print("Роли с таким индексом не существует")

#Проверка методов внутри класса
if __name__ == "__main__":
    role = RolesControllers("Admin")
    role.add()
    user = RolesControllers("User")
    user.add()
    print("------------")
    role.get
    #role.show(4)
    role.get = "Administrator"
    role.add()
    role.get
    role.update(2,"not Administrator")
    role.get
    role.delete(2)
    role.get