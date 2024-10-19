numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
n=0
for i in range(len(numbers)):
    if numbers[i]==None: n=i
average=[sum(numbers[:4]+numbers[5:])/len(numbers)]
new_numbers=numbers[:4]+average+numbers[5:]
print("Измененный список:", new_numbers)
