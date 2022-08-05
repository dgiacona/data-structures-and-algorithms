from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.animal_type == "dog":
            self.dog_queue.enqueue(animal)

        elif animal.animal_type == "cat":
            self.cat_queue.enqueue(animal)

        else:
            raise Queue.InvalidOperationError


    def dequeue(self, value):
        if value == "dog":
            return self.dog_queue.dequeue()

        if value == "cat":
            return self.cat_queue.dequeue()

        else:
            return None

class Dog:
    def __init__(self):
        self.animal_type = "dog"


class Cat:
    def __init__(self):
        self.animal_type = "cat"

