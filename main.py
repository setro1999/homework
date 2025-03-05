def bubble_sort(arr):
    """Функция для сортировки массива методом пузырька."""
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    print("Введите числа через пробел для сортировки:")
    try:
        # Получаем ввод от пользователя
        user_input = input()
        # Преобразуем ввод в список чисел
        numbers = [int(x) for x in user_input.split()]
    except ValueError:
        print("Ошибка: вводите только целые числа, разделённые пробелами.")
        return

    # Выводим исходный список
    print("Исходнfый список:", numbers)

    # Сортируем методом пузырька
    bubble_sort(numbers)

    # Выводим отсортированный список
    print("Отсортированный список:", numbers)


if __name__ == "__main__":
    main()
