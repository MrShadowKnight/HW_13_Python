# TASK №1

x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))
result = x ** y
print(f"{x} у степені {y} дорівнює {result}")

# TASK №2

count = 0

for num in range(100, 1000):
    digits = [int(digit) for digit in str(num)]
    if digits[0] == digits[1] or digits[0] == digits[2] or digits[1] == digits[2]:
        count += 1

print(f"Кількість чисел з двома однаковими цифрами: {count}")

# TASK №3

count = 0

for num in range(100, 10000):
    digits = set(str(num)) 
    if len(digits) == len(str(num)):  
        count += 1

print(f"Кількість чисел з усіма різними цифрами: {count}")

# TASK №4

def remove_digits(number, digits_to_remove):
    result = ''
    for digit in str(number):
        if digit not in digits_to_remove:
            result += digit
    return result

number = int(input("Введіть ціле число: "))
digits_to_remove = ['3', '6']

result = remove_digits(number, digits_to_remove)

print(f"Результат: {result}")