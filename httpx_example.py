# import httpx
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())
# httpx.get
#
#
# import httpx
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response.status_code)  # 201 (Created)
# print(response.json())       # Ответ с созданной записью
#
#
# data = {"username": "test_user", "password": "123456"}
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}
#
#
#
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# print(response.json())  # Заголовки включены в ответ
#
#
#
# import httpx
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())  # Данные первой задачи
# print(response2.json())  # Данные второй задачи
#
#
#
# import httpx
#
# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
#
# response = client.get("https://httpbin.org/get")
#
# print(response.json())  # Заголовки включены в ответ
# client.close()


import httpx

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())  # Заголовки включены в ответ
