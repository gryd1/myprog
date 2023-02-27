import pytest


@pytest.fixture()
def set_up():
    print('login')
    yield
    print('exit login')


@pytest.fixture(scope="module")
def some():
    print('Запускаем тестирование')
    yield
    print('Завершаем тестирование')
