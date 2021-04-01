# Python program to print positive Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print("Positive Numbers in the Range :")
# for loop & range() function
for num in range(start, end + 1):

	#condition
	if num >= 0:
		print( num, end = " ")
