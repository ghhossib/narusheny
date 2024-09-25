from Models.Users import *
class UsersConroller(Users):
    def __init__(self, login,password,phone,mail,fullname,role_id):
        super().__init__(login,password,phone,mail,fullname,role_id)

    users = []

    def add(self):
        self.users.append({'login': self.login, 'password': self.password})


    @property
    def get(self,login):
        for element in self.__login:
            print('вы авторизованы')