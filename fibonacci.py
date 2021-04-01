#Write a Python Program for Fibonacci numbers.

n = int(input("Enter the number of terms in Fibonacci Series: "))

n1 = 0
n2 = 1
sum = 0
count = 1

print("Fibonacci Series: ", end = " ")

while(count <= n):
  print(sum, end = " ")
  count += 1
  n1 = n2
  n2 = sum
  sum = n1 + n2
