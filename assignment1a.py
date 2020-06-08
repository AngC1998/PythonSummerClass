def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3.0

def letterGrade(avg):
    if avg >= 90 and avg <= 100:
        return "A"
    elif avg >= 80 and avg < 90:
        return "B"
    elif avg >= 70 and avg < 80:
        return "C"
    elif avg >= 60 and avg < 70:
        return "D"
    else:
        return "F"

name = input("Student name: ")
scoreOne = int(input("Test 1: "))
scoreTwo = int(input("Test 2: "))
scoreThree = int(input("Test 3: "))
avg = average(scoreOne, scoreTwo, scoreThree)
print("Avg: "+str(avg))
letter = letterGrade(avg)
print("Letter Grade: "+letter)