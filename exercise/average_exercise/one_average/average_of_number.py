my_file = open('./number_list.txt')
counter = 0
data_sum = 0
for line in my_file:
    counter += 1
    data_cleaning = float(line.strip())
    data_sum += data_cleaning
average = data_sum/counter
print(average)
result = open('./result.txt','w')
result.write(str(average))
result.close()