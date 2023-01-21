import types

def flat_generator(list_of_lists):
    cursor_list = 0 # Указатель на индекс списка
    cursor_element = 0 # Указатель на индекс элемента в вложенном списке   
    while cursor_list < len(list_of_lists): # Этот while используется для передвижения на список вперед, если внутренний while завершился. К cursor_list, выступающему в роли индекса, прибавляется единица и дальше цикл проходит по следующему списку.
        length_list = len(list_of_lists[cursor_list]) # Фиксируем длину вложенного списка
        while cursor_element < length_list: # Этот while используется для прохождения по вложенному списку. К cursor_element, выступающему в роли индекса, прибаляется единица и дальше цикл идёт по элементам влоаженного списка.
            item = list_of_lists[cursor_list][cursor_element] # Присваиваем item значение элемента в вложенном списке
            cursor_element += 1 # Прибавление единицы к показателю индекса(cursor.element) для последующего присваения item следующего элемента вложенного списка
            yield item # Возвращение item
        cursor_list += 1 # Прибавление единицы к показателю индекса списка(cursor_list) для продвижения к следующему, если предыдущий закончился
        cursor_element = 0 # Заново присваиваем 0 показателю индекса элемента(cursor_list), так как если этого не сделать, то он останется с тем же показателем, что и последний элемент вложенного списка, который цикл прошёл.
def test_2():

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
    test_2()
    