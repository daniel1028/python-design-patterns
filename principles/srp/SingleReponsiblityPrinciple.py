"""
Design pattern called, Single Reponsiblity Principle
In each class we should have relevant functions.

"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return '\n'.join(self.entries)


# load and save functions are irrelavnat to this class. It should be moved to new class
# def save(self, filename):
#     file = open(filename, 'w')
#     file.write(str(self))
#     file.close()
#
# def load(self):
#     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        filename = open(filename, 'w')
        filename.write(str(journal))
        filename.close()


j1 = Journal()
j1.add_entry("I feel very bad today")
j1.add_entry("I cried today")
j1.add_entry("All is well")
# print(j1)

filename = r'./journals.txt'
PersistenceManager.save_to_file(j1, filename)

with open(filename, 'r') as rh:
    print(rh.read())
