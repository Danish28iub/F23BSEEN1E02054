previous_number=0
for current_number in range(1, 11):
    current_sum = current_number + previous_number
    print(f"Sum of {current_number} and {previous_number} is: {current_sum}")
    previous_number = current_number
