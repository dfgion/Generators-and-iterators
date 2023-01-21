class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.length = len(list_of_list)

    def __iter__(self):
        print('Вход')
        self.cursor_list = 0 # Указатель на индекс списка
        self.cursor_element = 0 # Указатель на индекс элемента в вложенном списке 
        return self

    def __next__(self):
        while self.cursor_list < self.length: # Этот while используется для передвижения на список вперед, если внутренний while завершился. К self.cursor_list, выступающему в роли индекса, прибавляется единица и дальше цикл проходит по следующему списку.
            self.length_list = len(self.list_of_list[self.cursor_list]) # Фиксируем длину вложенного списка
            while self.cursor_element < self.length_list: # Этот while используется для прохождения по вложенному списку. К self.cursor_element, выступающему в роли индекса, прибаляется единица и дальше цикл идёт по элементам влоаженного списка.
                item = self.list_of_list[self.cursor_list][self.cursor_element] # Присваиваем item значение элемента в вложенном списке
                self.cursor_element += 1 # Прибавление единицы к показателю индекса(self.cursor.element) для последующего присваения item следующего элемента вложенного списка
                return item # Возвращение item
            self.cursor_list += 1 # Прибавление единицы к показателю индекса списка(self.cursor_list) для продвижения к следующему, если предыдущий закончился
            self.cursor_element = 0 # Заново присваиваем 0 показателю индекса элемента(self.cursor_list), так как если этого не сделать, то он останется с тем же показателем, что и последний элемент вложенного списка, который цикл прошёл.
        print('Выход')
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    