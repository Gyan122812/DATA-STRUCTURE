# def create_prefix_sum(arr):
#     n = len(arr)
#     prefix = [0] * n
#     prefix[0] = arr[0]
#     for i in range(1, n):
#         prefix[i] = prefix[i-1] + arr[i]
#     return prefix

# def range_sum(prefix, L, R):
#     if L == 0:
#         return prefix[R]
#     else:
#         return prefix[R] - prefix[L-1]

# # Example usage
# arr = [1, 3, 5, 7, 9]
# prefix = create_prefix_sum(arr)
# L, R = 1, 3  # Sum from index 1 to 3 (3+5+7=15)
# print("Sum of elements from index", L, "to", R, "is:", range_sum(prefix, L, R))

# def longest_unique_substring(s):
#     seen = set()
#     start = 0
#     max_len = 0
    
#     for end in range(len(s)):
#         while s[end] in seen:
#             seen.remove(s[start])
#             start += 1
#         seen.add(s[end])
#         max_len = max(max_len, end - start + 1)
    
#     return max_len

# # Example
# s = "abcabcbb"
# print("Length of longest unique substring:", longest_unique_substring(s))


# def majority_element(nums):
#     count = 0
#     candidate = None

#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)

#     return candidate

# # Example
# nums = [2,2,1,1,1,1,1,2,2]
# print("Majority Element:", majority_element(nums))


# def maxProduct(nums):
#     max_prod = min_prod = result = nums[0]

#     for num in nums[1:]:
#         temp = max_prod
#         max_prod = max(num, max_prod*num, min_prod*num)
#         min_prod = min(num, temp*num, min_prod*num)
#         result = max(result, max_prod)

#     return result

# # Example
# nums = [2,3,6,-2,4,1,5]
# print("Max Product Subarray:", maxProduct(nums))




# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def removeNthFromEnd(head, n):
#     dummy = ListNode(0, head)
#     fast = slow = dummy
    
#     for _ in range(n):
#         fast = fast.next
        
#     while fast.next:
#         fast = fast.next
#         slow = slow.next
        
#     slow.next = slow.next.next
#     return dummy.next

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# n = 3
# new_head = removeNthFromEnd(head, n)
# print("Linked List after removing the nth node from end: ",ListNode(0, head))

# # Print the modified linked list
# current = new_head
# while current:
#     print(current.val, end=" -> ")
#     current = current.next
# print("None")




# def getIntersectionNode(headA, headB):
#     if not headA or not headB:
#         return None
    
#     a, b = headA, headB
#     while a != b:
#         a = a.next if a else headB
#         b = b.next if b else headA
#     return a

# Example would involve creating intersecting linked lists

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# headA = ListNode(1, ListNode(2, ListNode(3)))
# headB = ListNode(6, ListNode(7, ListNode(8, headA)))  # Intersecting at node with value 2
# # headA: 1 -> 2 -> 3
# # headB: 6 -> 7 -> 8 -> 2 -> 3
# # The intersection node is the node with value 2

# intersection_node = getIntersectionNode(headA, headB)
# print("Intersection Node:", intersection_node.val if intersection_node else "No intersection")




# class TwoStacks:
#     def __init__(self, n):
#         self.arr = [0] * n
#         self.top1 = -1
#         self.top2 = n

#     def push1(self, x):
#         if self.top1 + 1 < self.top2:
#             self.top1 += 1
#             self.arr[self.top1] = x

#     def push2(self, x):
#         if self.top1 + 1 < self.top2:
#             self.top2 -= 1
#             self.arr[self.top2] = x

#     def pop1(self):
#         if self.top1 >= 0:
#             x = self.arr[self.top1]
#             self.top1 -= 1
#             return x
#         else:
#             return -1

#     def pop2(self):
#         if self.top2 < len(self.arr):
#             x = self.arr[self.top2]
#             self.top2 += 1
#             return x
#         else:
#             return -1

# # Example usage
# st = TwoStacks(10)
# st.push1(1)
# st.push2(10)
# st.push1(2)
# st.push2(20)
# st.push1(3)
# st.push2(30)
# st.push1(4)
# st.push2(40)

# print(st.pop1(), st.pop2())



# def isPalindrome(x):
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False
#     rev = 0
#     while x > rev:
#         rev = rev * 10 + x % 10
#         x //= 10
#     return x == rev or x == rev // 10

# # Example
# x = 123
# print("Is Palindrome:", isPalindrome(x))




def permute(arr, l, r):
    if l == r:
        print(arr[:])  # or print(''.join(s)) for strings
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            arr[l], arr[i] = arr[i], arr[l]  # backtrack

nums = [1, 2, 3]
n = len(nums)
permute(nums, 0, n - 1)

