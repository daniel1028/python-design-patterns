from abc import abstractmethod, ABC
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:

    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # Low - Level module

    def __init__(self):
        self.relations = []

    def add_parent_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # High level module

    # def __init__(self, relationships):
    #     relations = relationships.relations
    #
    #     for i, j, k in relations:
    #         print(f'{i.name} - {j} - {k.name}')
    #
    #     print("-" * 30)
    #     for r in relations:
    #         print(f'{r[0].name} | {r[1]} | {r[2].name}')
    #         print("=" * 30)

    # for r in relations:
    #     if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #         print(f'John has child {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has child {p}')


parent = Person("John")
child1 = Person("daniel")
child2 = Person("Mary")

relationships = Relationships()
relationships.add_parent_child(parent, child1)
relationships.add_parent_child(parent, child2)

research = Research(relationships)
