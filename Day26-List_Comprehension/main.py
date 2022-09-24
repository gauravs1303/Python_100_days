with open('f1.txt') as file:
    f1_data = file.read().splitlines()


with open('f2.txt') as file:
    f2_data = file.read().splitlines()

result = [int(item) for item in f1_data if item in f2_data]

print(result)