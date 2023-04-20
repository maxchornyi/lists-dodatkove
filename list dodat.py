#1
the_language = ['Ukrainian', 'English', 'Bulgarian', 'Norwegian', 'Latvian', 'German']
print(the_language)
print(sorted(the_language)) #за алфавітом
the_language.reverse()
print(the_language) #порядок навпаки
the_language.sort(reverse=True)
print(the_language) #спадання
#2
numbers_str = input("Введіть числа, розділені пропусками: ") #рядок введення
numbers = [int(num) for num in numbers_str.split()] #окремо, розділення
sum_of_numbers = sum(numbers) #сума чисел
print("Сума чисел: ", sum_of_numbers) #результат
#3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
message = ", ".join(cities[:-1]) + " and " + cities[-1] #додавання and
print(message)
#4
digits = input("Введіть 5 цифр через пробіл: ").split() #введення та розділення
reversed_digits = list(reversed(sorted(digits))) #зворотнє
print(reversed_digits)
number = int(''.join(reversed_digits))#Об'єднання елементів списку у число + відображення
print(number)
#5
sports = ['tennis', 'football', 'volleyball', 'basketball', 'polo']
sorted_sports = sorted(sports)
print(sorted_sports)
sports.reverse()
print(sports)
sports.sort()
print(sports)
sports.append('tennis')
print(sports)
sports.insert(2, 'nurse')
print(sports)
sports.pop()
print(sports)
sports.remove('nurse')
print(sports)
#6
raccoon=['Настя - трактор']
for i in raccoon:
    if i in 'Настя':
        print('Настя - самокат')
    else:
        print('Настя - трактор')

