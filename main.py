
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
chain = 0

if len(num1) > len(num2):
	print ('False')
else:
	for i in range(len(num2)):
		for j in range(len(num1)):
			if num2[i+j] == num1[j]:
				chain += 1
	if chain == len(num1):
		print("True")
	else:
		print("False")
# ******************************
# Make your Code
# ******************************

# print ('True') or ('False')
