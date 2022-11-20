"""
    Binary search
"""
from __future__ import annotations


def binary_search(listdata: list[int], item: int) -> tuple(int) | None:
    """
    Returns the position of an element in an ordered list
    and the number of iterations needed to calculate.
    """
    low = 0
    high = len(listdata) - 1
    counter_iteration = 0

    while low <= high:

        counter_iteration += 1
        mid = (low + high) // 2
        guess = listdata[mid]

        if guess == item:
            return item, counter_iteration
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def main() -> None:
    """
    Program entry point
    @return: None
    """
    length_of_list = list(range(int(input("Введите длину списка : "))))
    value = int(input("Введите число для поиска: "))
    print(binary_search(length_of_list, value))


if __name__ == "__main__":
    main()
