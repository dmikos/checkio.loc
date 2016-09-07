num = 4

print("Если число делится на 3 и 5, будет показано \"Fizz Buzz\";\nЕсли число делится \
     на 3, будет показано \"Fizz\";\nЕсли число делится на 5, будет показано \"Buzz\";")
print("Иначе,будет показано введенное число.")
print("Введено число", num)

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        number = "Fizz Buzz"
    elif number % 3 == 0:
    	number = "Fizz"
    elif number % 5 == 0:
    	number = "Buzz"

    return str(number)

print(checkio(num))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
