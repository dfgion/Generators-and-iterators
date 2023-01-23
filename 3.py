import types

class FlatIterator:
    def __init__(self, list_of_list):
        self.result = self._get_correct_list(list_of_list) # Вызываем функцию, которая возвращает один корректный список

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try: # Конструкция используется для завершения итерации в случае исключения list index out of range, так как мы присваиваем self.index значения без информации о длине списка
            item = self.result[self.index]
            self.index += 1
            return item 
        except:
            raise StopIteration
            
    def _get_correct_list(self, list_of_lists):
        result = []
        for element in list_of_lists:
            if isinstance(element, list):
                result.extend(self._get_correct_list(element))
            else:
                result.append(element)
        return result

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
