import mysql.connector

def execute_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='ваш_хост',
            port=ваш_порт,
            database='ваша_бд',
            user='ваш_пользователь',
            password='ваш_пароль',
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Задание 1: Посчитать количество поставщиков данного материала
def count_suppliers_of_material(connection, material_code):
    query = '''
        SELECT COUNT(DISTINCT SupplierCode)
        FROM StorageUnits
        WHERE MaterialCode = %s
    '''
    params = (material_code,)
    result = execute_query(connection, query, params)
    print(f"Количество поставщиков для материала {material_code}:")
    print(result[0]['COUNT(DISTINCT SupplierCode)'])

# Задание 2: Предоставить возможность добавления единицы хранения с указанием всех реквизитов
def add_storage_unit(connection, order_number, order_date, supplier_code, document_code, document_number,
                     material_code, material_account, unit_code, quantity, unit_price):
    query = '''
        INSERT INTO StorageUnits (OrderNumber, OrderDate, SupplierCode, DocumentCode, DocumentNumber,
                                  MaterialCode, MaterialAccount, UnitCode, Quantity, UnitPrice)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    params = (order_number, order_date, supplier_code, document_code, document_number, material_code,
              material_account, unit_code, quantity, unit_price)
    execute_query(connection, query, params)

# Задание 3: Вывести список поставщиков с указанием всех реквизитов данного материала на склад
def list_suppliers_of_material(connection, material_code):
    query = '''
        SELECT DISTINCT s.SupplierCode, sp.SupplierName, sp.INN, sp.LegalAddress, sp.BankAddress, sp.BankAccount
        FROM StorageUnits s
        JOIN Suppliers sp ON s.SupplierCode = sp.SupplierCode
        WHERE s.MaterialCode = %s
    '''
    params = (material_code,)
    result = execute_query(connection, query, params)
    print(f"Список поставщиков для материала {material_code} с указанием всех реквизитов:")
    print(result)

# Задание 4: Для указанного адреса банка посчитать количество поставщиков склада, пользующихся услугами этого банка
def count_suppliers_using_bank(connection, bank_address):
    query = '''
        SELECT COUNT(DISTINCT s.SupplierCode)
        FROM StorageUnits s
        JOIN Suppliers sp ON s.SupplierCode = sp.SupplierCode
        WHERE sp.BankAddress = %s
    '''
    params = (bank_address,)
    result = execute_query(connection, query, params)
    print(f"Количество поставщиков склада, пользующихся услугами банка по адресу {bank_address}:")
    print(result[0]['COUNT(DISTINCT s.SupplierCode)'])

# Подключаемся к базе данных
connection = connect_to_database()

if not connection:
    print("Не удалось подключиться к базе данных.")
else:
    try:
        # Задание 1
        material_code = 'ABC123'
        count_suppliers_of_material(connection, material_code)

        # Задание 2
        add_storage_unit(connection, 'ORD123', '2023-01-15', 'SUP456', 'DOC789', '123456', 'ABC123',
                         'MAT789', 'UNI987', 100, 10.5)

        # Задание 3
        list_suppliers_of_material(connection, 'ABC123')

        # Задание 4
        bank_address = 'Bank Street, 123, Cityville'
        count_suppliers_using_bank(connection, bank_address)

    except Exception as e:
        print(f"Error: {e}")

    # Закрываем соединение с базой данных
    connection.close()
