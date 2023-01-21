import types

def flat_generator(list_of_lists):
    for item in get_correct_list(list_of_lists):
        yield item
def get_correct_list(list_of_lists):
        result = []
        for element in list_of_lists:
            if isinstance(element, list):
                result.extend(get_correct_list(element))
            else:
                result.append(element)
        return result

def test_4():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_4()