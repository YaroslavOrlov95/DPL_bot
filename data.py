import sqlite3

class BotDB:

    def __init__(self, DPL):
        self.conn = sqlite3.connect(DPL)
        self.cursor = self.conn.cursor()

    def check_user(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM 'users' WHERE `id` = ?", (user_id,))
        return bool(len(result.fetchall()))


    def check_phone(self, user_id):
        """Получаем номер телефона юзера"""

        result = self.cursor.execute("SELECT phone_number FROM 'users' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def check_first_name(self, user_id):
        """Получаем имя юзера"""

        result = self.cursor.execute("SELECT name FROM 'users' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def check_username(self, user_id):
        """Получаем username юзера"""

        result = self.cursor.execute("SELECT username FROM 'users' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def company_name(self, user_id):
        """Получаем название компании юзера"""

        result = self.cursor.execute("SELECT company_name FROM 'users' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def status_order(self, user_id):
        """Получаем статус заказа юзера"""

        result = self.cursor.execute("SELECT status FROM 'orders' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def sequence_number(self, user_id):
        """Получаем порядковый номер заказа"""

        result = self.cursor.execute("SELECT sequence_number FROM 'orders' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def get_user_orders(self, user_id):
        """Получаем все заказы одного юзера"""

        result = self.cursor.execute("SELECT * FROM 'orders' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def get_id_order(self, user_id):
        """Получаем уникальный номер заказа"""

        result = self.cursor.execute("SELECT id_order FROM 'orders' WHERE `id` = ?", (user_id,))

        return result.fetchall()

    def get_phone_number_order(self, user_id):
        """Получаем номер телефона заказа"""

        result = self.cursor.execute("SELECT phone_nomer FROM 'orders' WHERE `id` = ?", (user_id,))
        return result.fetchall()

    def get_description_text_order(self, user_id):
        """Получаем тех. задание заказа"""

        result = self.cursor.execute("SELECT description_text FROM 'orders' WHERE `id` = ?", (user_id,))
        return result.fetchall()

    def get_status_order(self, user_id):
        """Получаем cтатус заказа"""

        result = self.cursor.execute("SELECT status FROM 'orders' WHERE `id` = ?", (user_id,))
        return result.fetchall()

    def add_order(self, user_id, id_order, phone_nomer, description_text):
        """Добавляем заказ в базу"""
        self.cursor.execute("INSERT INTO 'orders' ('id', 'id_order', 'phone_nomer', 'description_text') VALUES (?, ?, ?, ?)", (user_id, id_order, phone_nomer, description_text))
        return self.conn.commit()

    def add_user(self, user_id, first_name, username, phone_nomer, company_name):
        """Добавляем пользователя в базу"""
        self.cursor.execute("INSERT INTO `users` (`id`, `name`, `user_name`, 'phone_number', 'company_name') VALUES (?, ?, ?, ?, ?)", (user_id, first_name, username, phone_nomer, company_name))
        return self.conn.commit()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()

