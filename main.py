# average of N numbers
num = int(input("How many numbers are there? "))
total_sum = 0

for n in range(num):
    numbers = float(input("What is the number? "))
    total_sum += numbers

average = total_sum / num
print("The average is:", +average)




