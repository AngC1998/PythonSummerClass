import random

tNineMap = {
    'abc': '2',
    'def': '3',
    'ghi': '4',
    'jkl': '5',
    'mno': '6',
    'pqrs': '7',
    'tuv': '8',
    'wxyz': '9',
    ' ': '0'
}

words = {}

def decode(string):
    array = words.get(string)
    if array is None:
        return 'unable to decode'
    if len(array) == 1:
        return array[0]
    random_index = random.randint(0, len(array)-1)
    return array[random_index]

def encode(string):
    result = ''
    for c in string:
        for line in tNineMap:
            if c in line:
                result += tNineMap[line]
                break
    array = words.get(result)
    if array is None:
        array = []
    if string not in array:
        array.append(string)
    words[result] = array
    return result

def setUpDictionary():
    with open('words_alpha.txt') as word_list:
        for line in word_list.readlines():
            word = line
            encode(word)

def main():
    in_char = ''
    while in_char != 'x':
        print('e to encode')
        print('d to decode')
        print('x to exit')
        in_char = input('Enter in function: ')
        in_char = in_char.lower()
        if in_char == 'e':
            input_string = input('Input string: ')
            input_string = input_string.lower()
            print(encode(input_string))
            print(words)
        elif in_char == 'd':
            input_string = input('Input string: ')
            input_string = input_string.lower()
            print(decode(input_string))
        elif in_char == 'x':
            print('Good-bye')
        else:
            print('Invalid input. Try again')

setUpDictionary()
main()
