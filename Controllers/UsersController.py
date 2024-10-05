#В данном классе созданы методы для работы с атрибутами класса Users
from Models.Users import *

class UsersController(Users):
    def init(self,id,login,password,number,email,full_name,role_id):
        super().init(id,login,password,number,email,full_name,role_id)

    users = []
    #Методы регистрации, авторизации, вывод ФИО
    def add(self):
        self.users.append(
            {
                'id': self.id,
                'login': self.login,
                'password': self.password,
                'number': self.number,
                'email': self.email,
                'fullname': self.fullname,
                'role_id': self.role_id
            }
        )

    #Метод вывода списка Users
    @staticmethod
    def get():
        for element in UsersController.users:
            print(element)

    #Метод авторизации
    @staticmethod
    def login_user(input_login, input_password):
        for element in UsersController.users:
            if element['login'] == input_login and str(element['password']) == input_password:
                return True
            else:
                return False


    #Вывод имён всех пользователей
    @staticmethod
    def show_name():
        for element in UsersController.users:
            print(element['fullname'])

    #Метод вывода полного имени пользователя
    @staticmethod
    def show(id):
        for element in UsersController.users:
            if element['id'] == id:
                print(element['fullname'])

if __name__ == "__main__":
    User1 = UsersController(1,
                            'ivan',
                            12345,
                            666,
                            'ivan@iv.iv',
                            'Ivanov Ivan',
                            1)
    #Регистрация пользователя
    User1.add()
    UsersController.get()
    print(UsersController.login_user('ivan',12345))
    UsersController.show_name()
    UsersController.show(1)
