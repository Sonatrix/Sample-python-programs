def sayHello():
	print('hello world')
def square(no):
    return no * no

#print(square(-23))
#sayHello()
def reverse(word):
	return word[::-1]
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(reverse('testing'))
print(sorted(fruits,key = len,reverse = True))
def print_directory_contents(pathd):
	import os
	for schild in os.listdir(pathd):
		child = os.path.join(pathd,schild)
		if os.path.isdir(child):
			print_directory_contents(child)
		else:
			print(child)

print_directory_contents('/home/')
