##
# INSTRUCTIONS:
# 1. DO NOT rename the function names or change the parameters
# 2. Feel free to write helper functions in the HELPER FUNCTIONS area
# 3. DO NOT write new classes to help solve the problems
# 4. Make use of 'sandbox.py' to test/debug your code
# 5. I will test your code using my user generated files
# 6. Make use of the group chat & ask questions in the group chat
#
#
#

# HELPER FUNCTIONS
lazy_cache = {}
##
# write a function that adds the numbers between x and y inclusive
# return the sum of those numbers
# #
def part0(x, y):
    sum = 0
    for num in range(x, y+1):
        sum += num
    return sum


##
# write a function that checks if a  number is a perfect even
# this means that the number has no odd factors except 1
# returns True/False
def part1(num):
    if num % 2 == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            if i % 2 == 1:
                return False
    return True


##
# convert a number to a roman numeral string
# the number should be in range [0, 1000]
#
# returns uppercase string roman numeral string representation of num
# https://www.britannica.com/topic/Roman-numeral
def part2(num):
    if num == 0:
        return ""
    roman_num = ""
    num_M = num // 1000
    for i in range(0, num_M):
        roman_num += "M"
    num -= (num_M * 1000)
    if (num >= 900) and (num < 1000):
        roman_num += "CM"
        num -= 900
    if (num >= 500) and (num < 900):
        roman_num += "D"
        num -= 500
    if (num >= 400) and (num < 500):
        roman_num += "CD"
        num -= 400
    num_C = num // 100
    for i in range(0, num_C):
        roman_num += "C"
    num -= (num_C * 100)
    if (num >= 90) and (num < 100):
        roman_num += "XC"
        num -= 90
    if (num >= 50) and (num < 90):
        roman_num += "L"
        num -= 50
    if (num >= 40) and (num < 50):
        roman_num += "XL"
        num -= 40
    num_X = num // 10
    for i in range(0, num_X):
        roman_num += "X"
    num -= (num_X * 10)
    if num == 9:
        roman_num += "IX"
        num -= 9
    if (num >= 5) and (num < 9):
        roman_num += "V"
        num -= 5
    for i in range(0, num):
        roman_num += "I"
    return roman_num


##
# Write a T9 Encryption method that takes a string parameter
# and converts it to a numerical value using a phone keypad as a cypher
# @par
# abc -> 2
# def -> 3
# ghi -> 4
# jkl -> 5
# mno -> 6
# pqrs -> 7
# tuv -> 8
# wxyz -> 9
# <space> ->0
# needs to return a encoded string
# Ex: part3("alan") = 2526
def part3(original):
    string = ""
    for ch in original:
        if (ch == 'a') or (ch == 'b') or (ch == 'c'):
            string += '2'
        elif (ch == 'd') or (ch == 'e') or (ch == 'f'):
            string += '3'
        elif (ch == 'g') or (ch == 'h') or (ch == 'i'):
            string += '4'
        elif (ch == 'j') or (ch == 'k') or (ch == 'l'):
            string += '5'
        elif (ch == 'm') or (ch == 'n') or (ch == 'o'):
            string += '6'
        elif (ch == 'p') or (ch == 'q') or (ch == 'r') or (ch == 's'):
            string += '7'
        elif (ch == 't') or (ch == 'u') or (ch == 'v'):
            string += '8'
        elif (ch == 'w') or (ch == 'x') or (ch == 'y') or (ch == 'z'):
            string += '9'
        elif ch == " ":
            string += '0'
    return string


##
# Check if 2 texts are isomorphic (each letter maps to another)
# ex: paper and title are isomorphic
# p -> t
# a -> i
# p -> t
# e -> l
# r -> e
# returns True/False
def part4(text1, text2):
    char_map = {}
    if len(text1) != len(text2):
        return False
    for i in range(0, len(text1)):
        ch1 = text1[i]
        ch2 = text2[i]
        ch = char_map.get(ch1)
        if ch == None:
           char_map[ch1] = ch2
        elif ch != ch2:
           return False
    return True


##
# check if a string is a palindrome: (spelt the same both ways)
# ignore the case
# part5(car): False
# part5(bob): True
# returns True/False
#
# ##
def part5(text):
    beg_index = 0
    end_index = len(text) - 1
    while beg_index < end_index:
        char1 = text[beg_index]
        char2 = text[end_index]
        if char1 != char2:
            return False
        beg_index += 1
        end_index -= 1
    return True


##
# write the combination formula
# c(n, k) = n! / ((n-k)! * k!)
# returns the combination of 2 number
# needs to work for large numbers and cannot timeout
# ##
def part6(n, k):
    diff = n - k
    product = 1
    quotient = 1
    end = max(k, diff)
    end_two = min(k, diff)
    for i in range(n, end, -1):
        product *= i
    for i in range(end_two, 1, -1):
        quotient *= i
    return product / quotient


##
# write the permutation formula
# p(n, k) = n! / (n-k)!
# returns the permutation of 2 number
# needs to work for large numbers and cannot timeout
# ##
def part7(n, k):
    diff = n - k
    product = 1
    for i in range(n, diff, -1):
        product *= i
    return product
