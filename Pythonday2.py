count = 0
e_list = []

while count < 5:
    name = input('Enter your name: ')
    print(name, 'is awesome!')
    e_list.append(name)
    count += 1
    
for i in e_list:
    print(f'{i} has been added to the list')
