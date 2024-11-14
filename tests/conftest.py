"""Фикстуры для тестов"""

import pytest


def p(*args) -> None:
    """Печать на экран"""
    print(*args)


NEW_LINE = "\n"


@pytest.fixture()
def set_up():
    """Код: Открыть браузер и зайти на сайт"""
    p()
    p(f"{NEW_LINE}Вход в систему выполнен{NEW_LINE}")
    yield
    p()
    p("Выход из системы выполнен")


@pytest.fixture(scope="module")
def some():
    """Пояснение"""
    p()
    p(f"{NEW_LINE}Начало{NEW_LINE}")
    yield
    p()
    p("Завершение.")
