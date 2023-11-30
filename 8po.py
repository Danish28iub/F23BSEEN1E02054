list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
odd_numbers=[num for num in list1 if num % 2 != 0]
even_numbers=[num for num in list2 if num % 2==0]
new_list = odd_numbers + even_numbers
print(new_list)