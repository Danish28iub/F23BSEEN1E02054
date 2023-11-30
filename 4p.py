def check_first_last_same(numbers):
    return numbers[0] == numbers[-1]
x = [10, 20, 30, 40, 10]
y = [75, 65, 15, 25, 30]
result_x = check_first_last_same(x)
result_y = check_first_last_same(y)

print(f"Given list x: {x}\nResult x is {result_x}")

print(f"\nGiven list y: {y}\nResult y is {result_y}")