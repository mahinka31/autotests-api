import httpx

data = {
  "email": "mahinka31@example.com",
  "password": "QWERTY1234"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
user_response = httpx.get("http://localhost:8000/api/v1/users/me",  headers=headers)

print(user_response.status_code)
print(user_response.json())


