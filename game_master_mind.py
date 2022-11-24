"""
The game Mastermind
"""
import random


CHIPS = {1: 'green',
         2: 'gray',
         3: 'yellow',
         4: 'red',
         5: 'blue',
         6: 'white',
         7: 'orange',
         8: 'pink'}


def code_generator() -> list[int]:
    """ Generates a secret code value to be guessed """
    rez_code = [0, 0, 0, 0]
    for i in range(len(rez_code)):
        rez_code[i] = random.choice(list(CHIPS.keys()))
    return rez_code


def code_input() -> list[int]:
    """ Reads the code from the keyboard """
    flags_error = False
    while not flags_error:
        string_code = input('Entet code :')
        try:
            rez_code = string_code.split(' ')
            rez_code = list(map(int, rez_code))
        except ValueError:
            print('Input error')
            continue
        for i in rez_code:
            if 0 < i < 9 and isinstance(i, int):
                pass
            else:
                print('Input error')
                flags_error = False
                break
            flags_error = True
    return rez_code


def master(inputstring: str, code: list[int]) -> list[int]:
    """
    Compares the entered and the certificate code value.
    Returns the number of matches by position and value,
    as well as numbers (colors) that matched in position.
    """

    c_code = code.copy()
    red, white = 0, 0
    for i in inputstring:
        while i in c_code:
            if c_code[c_code.index(i)] != inputstring[c_code.index(i)]:
                white += 1
                c_code[c_code.index(i)] = 0
                break
            c_code[c_code.index(i)] = 0
            red += 1
    return [red, white]


def main() -> None:
    """ Program launch """
    code = code_generator()
    print('MASTERMIND')
    attemp = 0
    while attemp < 12:
        code_string = code_input()
        table = master(code_string, code)
        print(table, end=' ')
        attemp += 1
        print(f'attemp = {attemp}')
        if table[0] == 4:
            print('YOU WIN!')
            break
    print(f'Game over\nSecret code = {code}')


if __name__ == '__main__':
    main()
