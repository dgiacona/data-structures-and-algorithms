from data_structures.linked_list import LinkedList


class Hashtable:

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * self.size

    def set(self, key, value):
        # Arguments: key, value
        # Returns: nothing
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket

        drop = (key, value)
        bucket.insert(drop)

    def get(self, key):
        index = self.hash(key)
        if not self.buckets[index]:
            return None
        bucket = self.buckets[index]

        current = bucket.head
        # current is the head of the linked list, which is a node that is a pair of data
        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]
            current = current.next
        return None

    def contains(self, key):
        # return a boolean of whether given key is in the table
        return bool(self.get(key))

    # Didnt get to Keys or Hash
