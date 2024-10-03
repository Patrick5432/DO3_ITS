import unittest
import math
import sys
from random import randint

def example_1():
    number_1 = 3
    number_2 = number_1 ** 2 + 10 / 5  # 3**2 + 10/5 = 9 + 2 = 11.0
    number_3 = number_1 + number_2 % 2 + 1  # 3 + (11.0 % 2) + 1 = 3 + 1 + 1 = 5.0
    number_4 = number_1 // 3 + number_3  # 3//3 + 5.0 = 1 + 5.0 = 6.0
    return number_4

def example_2():
    string_4 = "Как говаривал один мой знакомый"
    string_5 = " по поводу кавычек в питоне: 'Да какая разница, какие использовать? Что вообще может пойти не так?'"
    string_6 = string_4 + string_5

    string_8 = '-' * 50
    string_7 = '''
Да и в целом то я с ним согласен.
Кажется, что никаких проблем быть не должно.
'''
    string_9 = string_8 + string_7
    return string_6, string_9

def example_3():
    string = ' I like administration of hospital   '
    exclamation_point = '!'
    exclamation_point *= 3

    string = string.strip()
    string = string[:12].upper()
    return f'{string}! Ох, так неожиданно и прияяятноооо.'

def example_4(input_value):
    if input_value.isdigit():
        return f'Твое число в степени два равно {int(input_value)**2}'
    else:
        return 'Ну я же просил ввести целое число! Ну камон!'

def example_5(input_number):
    random_number = randint(-10, 10)
    difference_numbers = input_number - random_number
    try:
        sqrt_number = round(math.sqrt(difference_numbers), 2)
        result = f'Корень из {difference_numbers} = {sqrt_number}'
    except ValueError:
        result = "Корень из отрицательного числа брать нельзя!"
    return random_number, difference_numbers, result

def example_6(test_string, index):
    try:
        element = test_string[index]
        return element
    except IndexError:
        return "Такого индекса нет в этой строке!"

def example_7(test_string, ind_1=None, ind_2=None, step=None):
    try:
        if ind_1 is None:
            ind_1 = 0
        if ind_2 is None:
            ind_2 = len(test_string)
        if step is None:
            step = 1

        if ind_1 > ind_2 or ind_1 > len(test_string) or ind_2 > len(test_string):
            raise IndexError("Какая-то фигня у вас с индексами!")
        return test_string[ind_1:ind_2:step]
    except IndexError:
        return "Какая-то фигня у вас с индексами!"


class TestExamples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(example_1(), 6.0)

    def test_example_2(self):
        string_6, string_9 = example_2()
        self.assertIn("Как говаривал один мой знакомый", string_6)
        self.assertTrue(string_9.startswith('-' * 50))

    def test_example_3(self):
        result = example_3()
        self.assertEqual(result, 'I LIKE ADMIN! Ох, так неожиданно и прияяятноооо.')

    def test_example_4(self):
        self.assertEqual(example_4("5"), 'Твое число в степени два равно 25')
        self.assertEqual(example_4("abc"), 'Ну я же просил ввести целое число! Ну камон!')

    def test_example_5(self):
        input_number = 5
        random_number, difference_numbers, result = example_5(input_number)
        if difference_numbers >= 0:
            self.assertTrue("Корень из" in result)
        else:
            self.assertEqual(result, "Корень из отрицательного числа брать нельзя!")

    def test_example_6(self):
        self.assertEqual(example_6("Тестовая строчка", 5), "в")
        self.assertEqual(example_6("Тестовая строчка", 50), "Такого индекса нет в этой строке!")

    def test_example_7(self):
        test_string = "Тестовая строчка"
        self.assertEqual(example_7(test_string, 1, 5, 1), "есто")
        self.assertEqual(example_7(test_string, 5, 1, 1), "Какая-то фигня у вас с индексами!")
        self.assertEqual(example_7(test_string, None, 5, None), "Тесто")


if __name__ == '__main__':
    unittest.main()
