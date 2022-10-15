"""
File: add2.py
Name: Yi-Ju Lu
------------------------
To add two ListNode and return a new ListNode of total
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    """
    1. make lists & str to store date in each ListNode
    2. sum up two numbers
    3. turn number to list, and use a new ListNode to connect each string in reverse direction
    4. return the new ListNode
    """
    list_1 = []
    list_2 = []
    str_1 = ''
    str_2 = ''
    cur_1 = l1  # cur to connect ListNode
    cur_2 = l2
    while cur_1 is not None:
        list_1.append(cur_1.val)  # to hold each data in ListNode
        cur_1 = cur_1.next        # go to next
    for i in range(len(list_1)):  # store str in reverse direction
        str_1 += str(list_1[-1 - i])
    num_1 = int(str_1)            # turn str into int

    while cur_2 is not None:
        list_2.append(cur_2.val)
        cur_2 = cur_2.next
    for j in range(len(list_2)):
        str_2 += str(list_2[-1 - j])
    num_2 = int(str_2)

    total = num_1 + num_2  # to sum up num_1 + num_2
    total_str = str(total)  # turning int to string

    # create a new ListNode and store last str as first ListNode
    new_node = ListNode((int(total_str[-1])), None)
    cur_total = new_node
    for i in range(len(total_str) - 1):  # to connect each ListNode reversely
        cur_total.next = ListNode(int(total_str[(-1 - i) - 1]), None)
        cur_total = cur_total.next
    cur_total.next = None
    #######################
    return new_node


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
