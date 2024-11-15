"""Модуль задает очередность запуска тестов."""

import pytest


@pytest.mark.run(order=5)
def test_method_1(set_up) -> None:
    """Метод 1."""
    print("test_method_1")
    assert True


@pytest.mark.run(order=6)
def test_method_2(set_up) -> None:
    """Метод 2."""
    print("test_method_2")
    assert True


@pytest.mark.run(order=4)
def test_method_3(set_up) -> None:
    """Метод 3."""
    print("test_method_3")
    assert True


@pytest.mark.run(order=3)
def test_method_4(set_up) -> None:
    """Метод 4."""
    print("test_method_4")
    assert True


@pytest.mark.run(order=2)
def test_method_5(set_up) -> None:
    """Метод 5."""
    print("test_method_5")
    assert True


@pytest.mark.run(order=1)
def test_method_6(set_up) -> None:
    """Метод 6."""
    print("test_method_6")
    assert True
