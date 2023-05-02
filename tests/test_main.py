from unittest import TestCase
from main import get_unique_id, request_percent, get_max_value

class TestUniqueId(TestCase):
    def test_1(self):
        x = {'user1': [213, 213, 213, 15, 213, 111],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
        expected = {98, 35, 15, 213, 54, 119, 111}
        result = get_unique_id(x)
        self.assertEqual(result, expected)

    def test_not_dict_in_arg(self):
        x = [213, 213, 213, 15, 213, 54, 54, 119, 119, 119, 213, 98, 98, 35]
        with self.assertRaises(AttributeError):
            get_unique_id(x)

class TestRequestPercent(TestCase):

    def test_1(self):
        list_requests = [
            'смотреть сериалы онлайн',
            'бухать не просыхая никогда',
            'новости спорта',
            'афиша кино',
            'курс доллара',
            'сериалы этим летом',
            'курс по питону',
            'сериалы про спорт',
        ]

        expected = {'Запросов с 2 словами': '38 процентов', 'Запросов с 3 словами': '50 процентов', 'Запросов с 4 словами': '12 процентов'}
        result = request_percent(list_requests)
        self.assertEqual(result, expected)

    def test_dict_in_return(self):
        list_requests = [
            'смотреть сериалы онлайн',
            'бухать не просыхая никогда',
            'новости спорта',
            'афиша кино',
            'курс доллара',
            'сериалы этим летом',
            'курс по питону',
            'сериалы про спорт',
        ]

        result = request_percent(list_requests)
        self.assertIsInstance(result, dict)

class TestGetMaxValue(TestCase):
    def test_negative_values(self):
        stats = {'facebook': -55, 'yandex': -120, 'vk': -115, 'google': -99, 'email': -42, 'ok': -98}
        expected = 'email'
        result = get_max_value(stats)
        self.assertEqual(result, expected)

    def test_str_in_result(self):
        stats = {'facebook': 36, 'yandex': 48}
        result = get_max_value(stats)
        self.assertIsInstance(result, str)






