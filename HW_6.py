# Написать функцию bubble_sort или selection_sort, принимающую в качестве входящего
# параметра не отсортированный список
# selection_sort

def selection_sort(arr):
    num_index = len(arr)
    for i in range(num_index):
        min_index = i
        for j in range(i + 1, num_index):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# lst = [23, 1, 450, 34, 615, 12, 33, 5, 17, 256, 14, 7, 813]
# selection_sort(lst)
# print(lst)

# Написать функцию binary_search, принимающую в качестве
# входящего параметра элемент для поиска и список в котором необходимо искать

def binar_search(arr, target_value):
    N = len(arr)
    ResultOK = False
    First = 0
    Last = N - 1

    while First <= Last:
        Middle = (First + Last) // 2
        if target_value == arr[Middle]:
            First = Middle  # не обязательное условие, взял из блок схемы
            Last = First  # не обязательное условие, взял из блок схемы
            ResultOK = True
            Pos = Middle # индекс элемента
            break

        else:
            if target_value > arr[Middle]:
                First = Middle + 1
            else:
                Last = Middle - 1

    if ResultOK == True:
        print(f'Element {target_value} was found, under index number: {Pos}')
        print(Pos)
    else:
        print(f'Element {target_value} was not found!')

lst = [23, 1, 450, 34, 615, 12, 33, 5, 17, 256, 14, 7, 813]
print(lst)

sorted_list = list(lst) # вводим новую переменную, чтобы видеть отличие
selection_sort(sorted_list)
print(sorted_list)
target_value = 256

binar_search(sorted_list, target_value)






