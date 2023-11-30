def print_half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
# Replace 5 with the number of rows you want in your half pyramid
print_half_pyramid(5)
