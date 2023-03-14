from LinkedList import LinkedList

# THe purpose of this file is to implement merge sort on a linked list

def merge_sort(linked_list):
    """Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Merge the sublists to create sorted sublists until only one remmains
    Takes O(kn log(n) )
    """

    if linked_list.size() ==1 or linked_list.head is None:
        return linked_list
    
    left,right = split(linked_list)
    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list)

def split(linked_list):
    # Divided the unsorted list at midpoint into sublists
    # Takes O(klog(n))

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    
    else:
        midpoint = linked_list.size()//2
        mid_node= linked_list.node_at_index(midpoint-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next
        mid_node.next = None
        
        return left_half,right_half

def merge(l , r):

    """
    Merges two linked lists while also sorting the data
    Return a new sorted merged list
    Take O(n)
    """

    ans = LinkedList()
    ans.add(0) # A placeholder head node

    current = ans.head

    left = l.head
    right = r.head

    while left or right:
        if left is None: # If the left list is empty or function is at the tail node, add the rest of the right list
            current.next = right
            right = right.next
        elif right is None: # If the right list is empty or function is at the tail node, add the rest of the left list
            current.next = left
            left = left.next
        else: 
            if left.data < right.data:
                current.next = left
                left=left.next
            elif left.data > right.data:
                current.next = right 
                right = right.next
                
        current = current.next

    ans.head = ans.head.next

    return ans

