class Node:

    #initialize node structure
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	#get minimum node from tree starting from this node
	def get_min_Node(self):
		current = self
		while current.left is not None:
			current = current.left
		return current

    #get maximum node from tree starting from this node
	def get_max_Node(self):
		current = self
		while current.right is not None:
			current = current.right
		return current

#insert node in binary tree
def insert(self,data):
		current = self
		if current is None:
			current = Node(data)
		if current.left is None and current.data>data:
			current.left = Node(data)
		elif current.right is None and current.data < data:
			current.right = Node(data)
		elif current.data >data:
			insert(self.left,data)
		else:
			insert(self.right,data)

#delete node from binary tree
def delete_Node(self,data):

	#check for none type
    if self is None:
        return self

    elif data>self.data:
        self.right = delete_Node(self.right,data)
    elif self.data>data:
        self.left = delete_Node(self.left,data)
    else:
        if self.left is None:
            tmp = self.right
            self = None
            return tmp
        elif self.right is None:
            tmp = self.left
            self = None
            return tmp
        tmp = self.right.get_min_Node()
        self.data  = tmp.data
        self.right = delete_Node(self.right,tmp.data)
    return self

#print inorder traversal of binary tree
def inorder(self):
	if self is None:
		return
	inorder(self.left)
	print(self.data)
	inorder(self.right)

#print preorder traversal of binary tree
def preorder(self):
	if self is None:
		return
	print(self.data)
	inorder(self.left)
	inorder(self.right)

#print postorder traversal of binary tree
def postorder(self):
	if self is None:
		return
	inorder(self.left)
	inorder(self.right)
	print(self.data)

#get height of tree
def height(self):
	if self is None:
		return 0
	else:
		lheight = height(self.left)
		rheight = height(self.right)

		if lheight > rheight:
			return lheight + 1
		else:
			return rheight + 1

#level order traversal of tree
def level_order(self):
	h = height(self)
	for i in range(1,h+1):
		print_level(self,i)

def print_level(self,level):

	if self is None:
		return
	if level == 1:
		print(self.data)
	else:
		if level > 1:
			print_level(self.left,level-1)
			print_level(self.right,level-1)
def printPaths(self,paths,pathLen):
	if self is None:
		return 
	else:
		paths.append(self.data)
		if self.right is None and self.left is None:
    			if len(paths) == pathLen+1:
				    print(paths)
		else:
				printPaths(self.left,paths,pathLen)
				printPaths(self.right,paths,pathLen)

a = Node(30)
insert(a,22)
insert(a,1)
insert(a,36)
# a.get_min_Node()
# a.get_max_Node()
# inorder(a)
# print('preorder')
preorder(a)
#delete_Node(a,22)

#print('post order')
#postorder(a)
#print('height of tree is %d'%height(a))
#print(height(a))
printPaths(a,[],height(a))
# print('level order traversal')
# print(level_order(a))
