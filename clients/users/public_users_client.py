from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

class UsersRequestDict(TypedDict):
    """
    Структура данных для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с эндпоинтами пользователей
    """

    def create_user_api(self, request: UsersRequestDict) -> Response:
        """
        Создает нового пользователя в системе.

        Выполняет POST-запрос к эндпоинту /api/v1/users для регистрации пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)