import pytest
from .users_repository import UsersRepository

@pytest.mark.asyncio
@pytest.mark.skip(reason="Insert in DB")
async def test_insert_user():
    new_user = {
        "user_name": "Nome de Teste",
        "age": 99,
        "uf": "SP"
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)

@pytest.mark.asyncio
@pytest.mark.skip(reason="Select in DB")
async def test_get_users_by_name():
    repo = UsersRepository()
    await repo.get_users_by_name("Nome de Teste")

@pytest.mark.asyncio
@pytest.mark.skip(reason="Delete in DB")
async def test_delete_user_by_name():
    repo = UsersRepository()
    await repo.delete_user_by_name("Nome de Teste")
    