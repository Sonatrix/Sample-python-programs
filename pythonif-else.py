n = int(raw_input().strip())
if n%2 != 0:
	print("Weird")
elif n%2 == 0 and n in [2,3,4,5]:
	print("Not Weird")
elif n%2==0 and n in range(6,20):
	print("Weird")
elif n%2 == 0 and n>20:
	print("Not Weird")


