
def bubble_sort(array: list[int]) -> list[int]:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                print(i, j, array)
    return array

array = [1, 114, 52, 2, 568 , 123, 5, 12, 2, 9]
print(bubble_sort(array))
