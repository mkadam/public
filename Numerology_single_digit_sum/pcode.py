# Program to print numbers having a specific single-digit total.
# Use case: Numerology needs single-digit numbers between 1 - 9.
# This program can be used to print numbers having single digit total as any specified number between 1-9
# Program needs start range, end range, and total to check as inputs.
# Useful for car number selection :)

# Define the range to check
start_range = 0 # Range start
end_range = 1000 # Range end
#Define the 
total_to_check = 1 #Should be set to any number between 1 - 9


#Function to find single digit sum of a given number
def single_digit_sum(number):
    # Function to calculate the sum of digits in a number, up to a single digit
    s = number
    while(s > 9):
        s = sum(int(digit) for digit in str(s))
    return s

#
#Simple loop which runs from start_range to end_range and prints numbers of which single digit sum is matching with total_to_check
#
print("Printing numbers in range ", start_range, "to", end_range, "with single digit total as:", total_to_check)

for num in range(start_range, end_range + 1):
    if single_digit_sum(num) == total_to_check:
        print("Total ", total_to_check, ": ", num)
    else:
        continue

print("done printing numbers in range ", start_range, "to", end_range, "with single digit total as:", total_to_check)
