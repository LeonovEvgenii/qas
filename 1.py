# class B():
# 	bb = 1

# 	def __init__(self, q):
# 		self.bb = q
# 		print("B")


# class A(B):

# 	b = 0

# 	def __init__(self, w):
# 		self.b = w
# 		super().__init__(w+2)
# 		print("A")






# obj = A(2)

# print(obj.b)
# print(obj.bb)


# def print_kwargs(**kwargs):
        # print(kwargs)
 
# print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)

# print([i + 2 for i in range(10)])
'''
function = lambda x,y: x*y
print(function(2,3))
'''
old_list = [1,2,3]
new_list = list(map(lambda x: x*45,old_list))
print(new_list)
a, b, c = input(), input(), input()
print(a,b,c)