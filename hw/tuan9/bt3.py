number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
              'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

list = []
dem = 1
while dem <= len(number_list):
    list.append(dem)
    dem+=1
numbers = dict(zip(number_list,list))

n = input('Input: ')
if n in numbers:
    print(numbers[n])
else:
    print('not found')