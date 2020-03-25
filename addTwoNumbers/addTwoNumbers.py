class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def comperList(A, B):
	while(A or B):
		if(A.val != B.val):
			return False
		else:
			A = A.next
			B = B.next

	return True

def addTwoNumbers(A, B):
	Return = ListNode(0)

	auxReturn = Return
	add = 0
	while(A or B):

		x = add
		add = 0

		if(A):
			x += A.val
			A = A.next

		if(B):
			x += B.val
			B = B.next

		if(x > 9):
			x -= 10
			add += 1

		auxReturn.next = ListNode(x)
		auxReturn =  auxReturn.next

	if(add > 0):
		auxReturn.next = ListNode(1)
		auxReturn =  auxReturn.next

	return Return.next


def testA():
	# 199
	A = ListNode(9)
	A.next = ListNode(9)
	A.next.next = ListNode(1)

	# 1
	B = ListNode(1)

	#200
	Result = ListNode(0)
	Result.next = ListNode(0)
	Result.next.next = ListNode(2)

	Return = addTwoNumbers(A, B)

	return comperList(Return,Result)

def testB():
	# 345
	A = ListNode(5)
	A.next = ListNode(4)
	A.next.next = ListNode(3)

	# 689
	B = ListNode(9)
	B.next = ListNode(8)
	B.next.next = ListNode(6)

	#1034
	Result = ListNode(4)
	Result.next = ListNode(3)
	Result.next.next = ListNode(0)
	Result.next.next.next = ListNode(1)

	Return = addTwoNumbers(A, B)

	return comperList(Return,Result)

def testC():
	# 345
	A = ListNode(5)
	A.next = ListNode(4)
	A.next.next = ListNode(3)

	# 689
	B = ListNode(9)
	B.next = ListNode(8)
	B.next.next = ListNode(6)

	#1034
	Result = ListNode(4)
	Result.next = ListNode(3)
	Result.next.next = ListNode(0)
	Result.next.next.next = ListNode(1)

	Return = addTwoNumbers(B, A)

	return comperList(Return,Result)

print(testA())
print(testB())
print(testC())