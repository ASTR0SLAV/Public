def get_sequence_numbers():
    sequence_numbers_input = input("Введите последовательность чисел через пробел: ")
    try:
        result_numbers = list(map(int, sequence_numbers_input.split()))
        if len(result_numbers) == 1:
            print("Вы ввели одно число. Введите !ПОСЛЕДОВАТЕЛЬНОСТЬ ЧИСЕЛ ЧЕРЕЗ ПРОБЕЛ! еще раз")
            return get_sequence_numbers()
        else:
            return result_numbers
    except ValueError:
        print("Это не правильный формат. Введите !ПОСЛЕДОВАТЕЛЬНОСТЬ ЧИСЕЛ ЧЕРЕЗ ПРОБЕЛ! еще раз")
        return get_sequence_numbers()


def get_number():
    number_input = input("Введите любое число: ")
    try:
        return int(number_input)
    except ValueError:
        print("Это не правильный формат. Введите !ОДНО ЧИСЛО! еще раз")
        return get_number()


def sorting(array_for_sorting):
    for i in range(len(array_for_sorting)):
        idx_min = i
        for j in range(i, len(array_for_sorting)):
            if array_for_sorting[j] < array_for_sorting[idx_min]:
                idx_min = j
        if i != idx_min:
            array_for_sorting[i], array_for_sorting[idx_min] = array_for_sorting[idx_min], array_for_sorting[i]
    return array_for_sorting


def find_element_position(array, element, left, right):
    if left > right:
        print("Условие не выполняется, место где предыдущее число меньше " + str(
            element) + ", а последующее больше или равно, не найдено")
        return False

    middle = (right + left) // 2
    if middle + 1 < len(array):
        if array[middle] < element and array[middle + 1] >= element:
            print("Позиция элемента: " + str(middle))
            return middle
        elif element <= array[middle]:
            return find_element_position(array, element, left, middle - 1)
        else:
            return find_element_position(array, element, middle + 1, right)
    else:
        print("Условие не выполняется, место где предыдущее число меньше " + str(
            element) + ", а последующее больше или равно, не найдено")


sequenceNumbers = get_sequence_numbers()
number = get_number()
sorted_array = sorting(sequenceNumbers)
position_element = find_element_position(sorted_array, number, 0, len(sequenceNumbers) - 1)
