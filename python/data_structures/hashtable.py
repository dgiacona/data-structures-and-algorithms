from data_structures.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * self.size

    def get(self, key):
        # for bucket in self.buckets:
        #     key_value = self.contains(key)
        #     if bucket:
        #         if key_value:
        #             current = bucket.head
        #             while current:
        #                 if key == current.value[0]:
        #                     return current.value[1]
        #                 current = current.next
        # return None
        index = self.hash(key)
        bucket = self.buckets[index])

        if not bucket:
            return None

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next

        return None

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket

        key_value_pair = (key, value)
        bucket.insert(key_value_pair)

    def contains(self, key):
        ## return a boolean of whether given key is in the table
        return bool(self.get(key))

    def keys(self):
        ## return all keys in the table
        all_keys = set()
        for item in self.buckets:
            if item:
                current_node = item.head
                while current_node:
                    all_keys.add(current_node.value[0])
                    current_node = current_node.next
        return all_keys

    def hash(self, key):
        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)
        primed = sum_of_chars * 971
        index = primed % self.size
        return index
