from faker import Faker


class PersonDataGenerate:
    def __init__(self):
        self.fake = Faker()

    def get_admin(self):
        """
        Получение данных админа\зарегистрированного пользователя
        :return:
        """
        admin = {
            'username': 'Deni',
            'email': 'fetoev@mail.ru',
            'password': 'TesT2024'
        }
        return admin

    def get_random_person(self):
        """
        Создание и получение рандомного пользователя
        :return:
        """
        username = self.fake.user_name()
        password = self.fake.password()
        email = self.fake.email()
        fake_person = {
            'username': username,
            'password': password,
            'email': email
        }
        return fake_person
