class Node:
    def __int__(self, data):
        self.data = data
        self.next = None


def check_palindrome(head):
    # l = length(head)
    t1 = head
    mid = l / 2
    isPalindrome = True

    for i in range(mid):
        t1 = t1.next

    t2 = t1.next
    t2.next = None
    t1.next = None

    while t2.next != None:
        if t2.data == t1.data:
            isPalindrome = True
        else:
            isPalindrome = False

        t1 = t1.next
        t2 = t2.next
    return isPalindrome


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        head.next = data
        last = last.next
    return head


arr = [9, 2, 3, 3, 2, 9, -1]
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("pali")
else:
    print("not")
