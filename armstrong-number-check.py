# The Checking of Armstrong Numbers 

number = int(input("Enter a number: "))
num_digits = len(str(number))
sum_of_powers = 0

temp = number
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

if sum_of_powers == number:
    print("🎉 Yes! It's an Armstrong Number.")
else:
    print("❌ Nope, not an Armstrong Number.")
