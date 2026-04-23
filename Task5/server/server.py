from ariadne import make_executable_schema, QueryType, ObjectType
from ariadne.asgi import GraphQL
import uvicorn

# 1. Определение схемы (SDL)
type_defs = """
type Query {
  client(id: ID!): Client
}

type Client {
  id: ID!
  name: String
  age: Int
  documents: [Document!]!
  relatives: [Relative!]!
}

type Document {
  id: ID!
  type: String
  number: String
  issueDate: String
  expiryDate: String
}

type Relative {
  id: ID!
  relationType: String
  name: String
  age: Int
}
"""

# 2. Имитация базы данных
DATABASE = {
    "clients": {
        "1": {"id": "1", "name": "Иван Иванов", "age": 35},
        "2": {"id": "2", "name": "Анна Петрова", "age": 28},
    },
    "documents": {
        "1": [
            {"id": "d1", "type": "Passport", "number": "4500 123456", "issueDate": "2010-05-20", "expiryDate": "2030-05-20"},
            {"id": "d2", "type": "Driver License", "number": "9900 654321", "issueDate": "2015-11-10", "expiryDate": "2025-11-10"}
        ],
        "2": [
            {"id": "d3", "type": "Passport", "number": "4600 789012", "issueDate": "2020-01-15", "expiryDate": "2040-01-15"}
        ]
    },
    "relatives": {
        "1": [
            {"id": "r1", "relationType": "Wife", "name": "Мария Иванова", "age": 32},
            {"id": "r2", "relationType": "Son", "name": "Алексей Иванов", "age": 5}
        ],
        "2": []
    }
}

# 3. Настройка резолверов
query = QueryType()
client_type = ObjectType("Client")

@query.field("client")
def resolve_client(*_, id):
    return DATABASE["clients"].get(id)

@client_type.field("documents")
def resolve_client_documents(client_obj, *_):
    # client_obj — это словарь клиента, возвращенный выше
    return DATABASE["documents"].get(client_obj["id"], [])

@client_type.field("relatives")
def resolve_client_relatives(client_obj, *_):
    return DATABASE["relatives"].get(client_obj["id"], [])

# 4. Создание исполняемой схемы
# snake_case_fallback_resolvers позволяет автоматически мапить поля, 
# если их имена совпадают с ключами в словарях
schema = make_executable_schema(type_defs, query, client_type)
#schema = make_executable_schema(type_defs, query, client_type, snake_case_fallback_resolvers)

# 5. Инициализация ASGI приложения
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    print("🚀 GraphQL сервер запущен на http://localhost:8080")
    uvicorn.run(app, host="0.0.0.0", port=8080)

