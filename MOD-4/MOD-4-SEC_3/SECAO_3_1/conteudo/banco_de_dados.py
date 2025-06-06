# STEP 1 ============================================== :
# from pymongo import MongoClient

# # Por padrão o host é localhost e porta 27017
# # Estes valores podem ser modificados passando uma URI
# # client = MongoClient("mongodb://localhost:27017/")
# client = MongoClient()

# STEP 2 ============================================== :
# from pymongo import MongoClient

# client = MongoClient()
# # o banco de dados catalogue será criado se não existir
# db = client.catalogue
# # a coleção books será criada se não existir
# students = db.books
# client.close()  # fecha a conexão com o banco de dados

# STEP 3 ============================================== :
# from pymongo import MongoClient

# client = MongoClient()
# db = client.catalogue
# # book representa um dado obtido na raspagem
# book = {
#     "title": "A Light in the Attic",
# }
# document_id = db.books.insert_one(book).inserted_id
# print(document_id)
# client.close()  # fecha a conexão com o banco de dados

# STEP 4 ============================================== :
from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
documents = [
    {
        "title": "A Light in the Attic",
    },
    {
        "title": "Tipping the Velvet",
    },
    {
        "title": "Soumission",
    },
]
db.books.insert_many(documents)

# busca um documento da coleção, sem filtros
print(db.books.find_one())

# busca utilizando filtros
for book in db.books.find({"title": {"$regex": "t"}}):
    print(book["title"])
client.close()  # fecha a conexão com o banco de dados


# STEP 6 ============================================== :
# from pymongo import MongoClient


# with MongoClient() as client:
#     db = client.catalogue
#     for book in db.books.find({"title": {"$regex": "t"}}):
#         print(book["title"])
