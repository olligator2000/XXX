

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://porshina1992:Qq1111111111@cluster0.h5gxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

###############################################################################################


# Create a new client and connect to the server
# client = MongoClient(uri)
#
# # Send a ping to confirm a successful connection
# # try:
# #     client.admin.command('ping')
# #     print("Pinged your deployment. You successfully connected to MongoDB!")
# # except Exception as e:
# #     print(e)
#
# db = client["scool"]
# print(db)
#
# students = db["students"]
#
# # students.insert_one({ "name": "Alice", "age": 25, "profession": "Engineer" })
# # students.insert_many([{ "name": "Mike", "age": 21, "profession": "Engineer" },
# #                      { "name": "Bob", "age": 23, "profession": "Engineer" },
# #                      { "name": "Jone", "age": 24, "profession": "Engineer" }])
# for i in students.find():
#     print(i)
#
# students.update_many({ "name": "Alice" }, { "$set": { "age": 27 } })

############################################################################################### 2
# Задача 2: Агрегирование данных в MongoDB
# Создайте базу данных company и коллекцию employees. Вставьте данные о сотрудниках, включая их имя, отдел и зарплату.\
# Используйте агрегирование для подсчета общей суммы зарплаты по каждому отделу.

# client = MongoClient(uri)
#
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#
#     db = client["company"]
#     employees = db["employees"]
#
#     # list_of_employees = [
#     #     {"name": "Alex", "departament": "Бухглатерия", "salary": 45000},
#     #     {"name": "Anna", "departament": "IT", "salary": 159000},
#     #     {"name": "Maxim", "departament": "Кадры", "salary": 87000},
#     #     {"name": "Oleg", "departament": "Бухглатерия", "salary": 16000},
#     #     {"name": "Alice", "departament": "Кадры", "salary": 34000},
#     #     {"name": "Samvel", "departament": "IT", "salary": 120000},
#     # ]
#     #
#     # employees.insert_many(list_of_employees)
#     #
#     # for i in employees.find():
#     #     print(i)
#
#     pipeline = [
#         {
#             "$group": {
#                 "_id": "$departament",
#                 "total_salary": {"$sum": "$salary"}
#             }
#         },
#         {
#             "$sort": {"_id": 1}
#         }
#     ]
#
#     result = employees.aggregate(pipeline)
#
#     for i in result:
#         print(i)
#
# except Exception as e:
#     print(e)


###############################################################################################
# Задача 1: Подсчет среднего возраста студентов по факультетам
# Условие: Создайте базу данных university и коллекцию students.
# Вставьте данные о студентах, включая имя, факультет и возраст.
# Используйте агрегацию, чтобы подсчитать средний возраст студентов для каждого факультета.

# client = MongoClient(uri)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#
#     db = client["university"]
#     students = db["students"]
#
#     # list_of_students = [
#     #     # {"name": "Alex", "fakulty": "ФВТ", "age": 22},
#     #     {"name": "Anna", "fakulty": "ФЭ", "age": 24},
#     #     {"name": "Maxim", "fakulty": "ФРТ", "age": 25},
#     #     {"name": "Oleg", "fakulty": "ФЭ", "age": 21},
#     #     {"name": "Alice", "fakulty": "ФРТ", "age": 23},
#     #     {"name": "Samvel", "fakulty": "ФВТ", "age": 26},
#     # ]
#
#     # students.insert_many(list_of_students)
#
#     pipeline = [
#         {
#             "$group": {
#                 "_id": "$fakulty",
#                 "avg_age": {"$avg": "$age"}
#             }
#         },
#         {
#             "$sort": {"_id": -1}
#         }
#     ]
#
#     result = students.aggregate(pipeline)
#
#     for i in result:
#         print(i)
#
# except Exception as e:
#     print(e)


###############################################################################################
# Задача 2: Подсчет количества товаров по категориям
# Условие: Создайте базу данных store и коллекцию products.
# Вставьте данные о товарах (название, категория, цена).
# Подсчитайте количество товаров в каждой категории.

# client = MongoClient(uri)
#
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#
#     db = client["store"]
#     products = db["products"]
#
#     # list_of_products = [
#     #     {"name": "Яблоко", "категория": "Фрукты", "price": 120},
#     #     {"name": "Апельсин", "категория": "Фрукты", "price": 200},
#     #     {"name": "Огурцы", "категория": "Овощи", "price": 300},
#     #     {"name": "Помидоры", "категория": "Овощи", "price": 400},
#     #     {"name": "Свинина", "категория": "Мясные продукты", "price": 400},
#     #     {"name": "Говядина", "категория": "Мясные продукты", "price": 450},
#     #     {"name": "Индейка", "категория": "Мясные продукты", "price": 500},
#     #     {"name": "Хлеб Белый Старожиловский", "категория": "Хлебобулочные", "price": 65},
#     #     {"name": "Хлеб Белый Скопинский", "категория": "Хлебобулочные", "price": 67},
#     #     {"name": "Хлеб Черный Дарницкий", "категория": "Хлебобулочные", "price": 63},
#     #     {"name": "Хлеб Черный Коломенский", "категория": "Хлебобулочные", "price": 68},
#     #     {"name": "Колбаса Докторская", "категория": "Колбасные изделия", "price": 300},
#     #     {"name": "Колбаса Докторская", "категория": "Колбасные изделия", "price": 300},
#     #     {"name": "Пельмени Мироторг 1 кг", "категория": "Полуфабрикаты", "price": 250},
#     #     {"name": "Пельмени Славянские 500гр", "категория": "Полуфабрикаты", "price": 340},
#     #     {"name": "Яйцо", "категория": "Яйца", "price": 120},
#     #     {"name": "Макороны 5кг", "категория": "Макаронные изделия", "price": 500},
#     #     {"name": "Макороны 1кг ", "категория": "Макаронные изделия", "price": 200},
#     #     {"name": "Макороны 400гр", "категория": "Макаронные изделия", "price": 80},
#     # ]
#
#     # products.insert_many(list_of_products)
#
#     pipeline = [
#         {
#             "$group": {
#                 "_id": "$категория",
#                 "sum_name": {"$sum": 1}
#             }
#         },
#         {
#             "$sort": {"_id": -1}
#         }
#     ]
#
#     result = products.aggregate(pipeline)
#
#     for i in result:
#         print(i)
#
# except Exception as e:
#     print(e)


###############################################################################################
# Задача 5: Общая стоимость товаров по брендам с фильтром
# Условие: Создайте базу данных warehouse и коллекцию items.
# Вставьте данные о товарах (название, бренд, цена).
# Подсчитайте общую стоимость товаров для каждого бренда, но только для товаров дороже 1000.

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client["warehouse"]
    items = db["items"]

    # list_of_items = [
    #     {"name": "Джинсы", "brand": "Адидас", "price": 120},
    #     {"name": "Майка", "brand": "Адидас", "price": 200},
    #     {"name": "Кросовки", "brand": "Адидас", "price": 300},
    #     {"name": "Кросовки", "brand": "Рибок", "price": 400},
    #     {"name": "Майка", "brand": "Рибок", "price": 400},
    #     {"name": "Джинсы", "brand": "Пранди", "price": 450},
    #     {"name": "Майка", "brand": "Пранди", "price": 500},
    #
    # ]
    #
    # items.insert_many(list_of_items)

    pipeline = [
        {
            "$match": {
                "price": {"$gt": 300}
            }
        },
        {
            "$group": {
                "_id": "$brand",
                "sum_price": {"$sum": "$price"}
            }
        },
        {
            "$sort": {"_id": -1}
        }
    ]

    result = items.aggregate(pipeline)

    for i in result:
        print(i)

except Exception as e:
    print(e)
