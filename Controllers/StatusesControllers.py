#Данный класс используется для обработки атрибутов Statuses
from Models.Statuses import Statuses
class StatusesController(Statuses):
    def init(self, id,status):
        super().init(id,status)

    #Для обработки значений защищённых атрибутов

    statuses = [] #список (массив) в котором хранятся словари со значениями атрибутов класса Statuses
    #методы CRUD
    #метод создания
    def add(self):
        self.statuses.append({'id' :self.id, 'status':self.status})

    #Если метод не зависит от объектов класса
    #его можно объявить статическим импользуем декоратор @staticmethod
    #Метод вывода всех записей из списка Statuses
    @property
    def get(self):
        for element in self.statuses:
            print(element)

    #Статический метод
    @staticmethod
    def get_static():
        for element in StatusesController.statuses:
            print(element)

    #Изменение значений в словаре по id
    #метод изменения id
    def update_id(self,id,new_id):
        if id <= len(self.statuses):
            self.statuses[id-1]['id'] = new_id
            print(f'id Статуса {id} изменено на {new_id}')
        else:
            print("нет такого статуса с id  = ", id)

    # Метод изменения статуса
    def update_status(self, id, new_status):
        for element in self.statuses:
            if element['id'] == id:
                element['status'] = new_status
        print(f"Статус изменён на {new_status}")

    def update_id_alternative(self,id, new_id):
        for element in self.statuses:
            if element['id'] == id:
                element['id'] = new_id
        print(f"ID изменён на {new_id}")

    #Метод изменения и статуса и id
    #Статический метод - метод которы не имеет доступа к объекту
    def update(self, id,new_id,new_status):
        self.update_status(id,new_status)
        self.update_id_alternative(id, new_id)

    #Удаление словоря из списка statuses по id
    #В цикле переменной element_list при каждой итерации (повторяющееся действия) будет присвоено число от 0 до индекса последнего элемента
    # range(len(self.statuses)) - определяет длинну списка
    #уловие используется для нахождения в каждом элементе списка id из параметра метода delete
    #если такой id найден, будет удалён элемент из списка
    def delete(self,id):
        for element_list in range(len(self.statuses)):
            if id == self.statuses[element_list]['id']:
                del self.statuses[element_list]
                print("Запись удалена")





if __name__ == "__main__":
    new_status = StatusesController(1, 'Новое')
    #print(new_status.statuses)
    new_status.add()
    #print(new_status.statuses)
    new_new_status = StatusesController(2,'В работе')
    new_new_status.add()
    #print(new_new_status.statuses)
    #print(StatusesController.statuses) #обращение к списку класса через название класса
    new_new_status.get
    print("--------------------------")
    cancel_status = StatusesController(3,"Отклонено")
    cancel_status.add()
    cancel_status.get
    cancel_status.update_id(3,4)
    cancel_status.get
    cancel_status.update_status(4,'очень отклонено')
    cancel_status.get
    cancel_status.update(4,5,'о-х-х-х')
    cancel_status.get
    print("----------------------")
    new_status.get
    print("-----Статический метод----------")
    StatusesController.get_static()
