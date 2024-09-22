import mysql.connector
from mysql.connector import Error

class DBhelper:
    
    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="",
                database="student"
            )
            self.cursor = self.conn.cursor()
            print('Connected to database...')
        except Error as e:
            print(f'Error occurred: {e}')

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print('Connection closed.')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    def register(self,name,marks,email):
        try:
            self.cursor.execute('''INSERT INTO `student_table` (`id`, `name`, `marks`, `email`) 
                                VALUES (NULL, '{}', '{}', '{}');'''.format(name,marks,email))
            self.conn.commit()
            return 1
        except Error as e:
            print(f'Error occurred: {e}')
    def search(self, email):
        query = '''SELECT * FROM student_table WHERE email LIKE '{}' '''.format(email)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def update(self,name,marks,email,id):
        
        try:
            self.cursor.execute('''
                            UPDATE `student_table` SET `name` = '{}',`marks`='{}',`email`='{}' WHERE `student_table`.`id` = {};
                            '''.format(name,marks,email,id))
            self.conn.commit()
            return 1
        except Error as e:
            print(f'error occured as {e}')
    def delete(self,id):
        try:
            self.cursor.execute('''DELETE FROM `student_table` WHERE `student_table`.`id` = {} '''.format(id))
            self.conn.commit()
            return 1
        except Error as e:
            print(f'Error Occured as {e}')
    def get_all(self):
        try:
            self.cursor.execute('''SELECT * FROM `student_table`;''')
            data=self.cursor.fetchall()
            return data
        except Error as e:
            print(f'Error Occured as {e}')