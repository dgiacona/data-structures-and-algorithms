from data_structures.linked_list import LinkedList

def zip_lists(a, b):

    list_one = a.head
    list_two = b.head
    while list_two and list_one:
        a.append(list_one.value, list_two.value)
        list_one = list_one.next
        if list_one.next:
            list_one = list_one.next
        list_two = list_two.next

    if list_one is None or list_two is None:
        if list_two:
            return b
        if list_one:
            return a

    return a

