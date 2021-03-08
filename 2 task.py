"""

Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем
включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические
операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.

"""

list1 = [i ** 3 for i in range(1, 1001) if i % 2 != 0]
numbers_sum = 0
for number in list1:
    digits_sum = 0
    number_for_operation = number            # перевод в другую переменную для того, чтобы можно было проще брать число в сумму, если оно подходит

    while number_for_operation != 0:
        digits_sum += number_for_operation % 10
        number_for_operation = number_for_operation // 10

    if digits_sum % 7 == 0:
        numbers_sum += number
print(numbers_sum)

numbers_sum = 0

for number in list1:
    number += 17
    digits_sum = 0
    number_for_operation = number

    while number_for_operation != 0:
        digits_sum += number_for_operation % 10
        number_for_operation = number_for_operation // 10

    if digits_sum % 7 == 0:
        numbers_sum += number
print(numbers_sum)
