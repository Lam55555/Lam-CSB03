numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
         'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}


def solama(n):
    if n in numbers:
        return print(numbers[n])
    else:
        return print('Khong tim thay')
y = str(input('Input: '))  
solama(y)  
        