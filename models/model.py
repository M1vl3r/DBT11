from connection.connection import connection

class Model:

    # метод вывода данных из таблицы

    def myGetCursor(self, query):
        with connection().cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get(self, nameTable):
        query = "SELECT * FROM %s" % nameTable
        return self.myGetCursor(query)

    def delete(self, table, id):
        with connection().cursor() as cursor:
            queries_delete_rows = f"DELETE FROM %s WHERE ID = %s" % (table, id)
            cursor.execute(queries_delete_rows)
            connection().commit()
        connection().close()
        print("запись удалена")

    def add(self, table, str, *values):
        with connection().cursor() as cursor:
            print(f"INSERT INTO {table} ({str}) VALUES {values}")
            query = f"INSERT INTO {table} ({str}) VALUES {values}"
            cursor.execute(query)
        connection().close()
        print(f"Новая запись в таблицу {table} добавлена")

    def update(self, table, id, field, values):
        with connection().cursor() as cursor:
            print(f"UPDATE {table} set {field} = '{values}' where id = {id}")
            queries_update = f"UPDATE {table} set {field} = '{values}' where id = {id}"
            cursor.execute(queries_update)
            connection().commit()
        connection().close()
        print("Запись обновлена")

    def getOneField(self,table,field):
        with connection().cursor() as cursor:
            select_one_field = f"SELECT {field} FROM {table}"
            cursor.execute(select_one_field)
            return cursor.fetchall()
        connection().close()


    def countAboutBanks (self, bank):
        with connection().cursor() as cursor:
            query = f"select COUNT(*) as count from suppliers where suppliers.Bank = {bank}"
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()