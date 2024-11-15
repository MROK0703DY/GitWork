"""Тестирование второй версии письма"""

import pytest


def p(*args) -> None:
    """Код: Вывод сообщения в консоль"""
    print(*args)


NEW_LINE = "\n"


def test_sending_mail_3(set_up, some, tear_down) -> None:
    """Код: Отправить письмо адресату"""
    p("Повестка отправлена")


def test_sending_mail_4(set_up, some, tear_down) -> None:
    """Код: Отправить письмо по адресу из приказа"""
    p("Рассылка благодарственности отправлена")


@pytest.fixture()
def tear_down() -> None:
    """Код: Завершение работы. Выход из системы"""
    p()
    p("Завершение работы. Не забудьте выключить свет")
