class Person:
    # class name begins with capital letter
    """
    A class representing a person
    """
    pass

    def __init__(self, name, age):
        """
        Construct a Person object
        """
        # attribute: a piece of data associated with object
        # self is a special argument that refer to object itself
        # double underscore is a special method called constructor
        self.name = name
        self.age = age
        self.friends = []

    def introduce_self(self):
        """
        Prints out a self introduction
        """
        print(f"Hi I'm {self.name} and I'm {self.age} years old.")
        if len(self.friends) > 0:
            self.introduce_friends()
        else:
            print("I prefer to operate alone")
        print()

    def introduce_friends(self):
        """
        Prints out friends
        """
        print("\tMy friends are:")
        for friend in self.friends:
            print("\t\t"+friend.name)
        print("The actual data in my firnds list is:")
        print(self.friends)
        # [<person.Person object at 0x1050b3f40>, <person.Person object at 0x1050e5840>]

    def befriend(self, new_friend):
        """
        Befriend a person
        """
        print(f"Hi there {new_friend.name}")
        self.add_friend(new_friend)
        # endless recursion: new_friend.befriend(self)
        new_friend.add_friend(self)

    def add_friend(self, new_friend):
        """
        Add friend to friends list
        """
        self.friends.append(new_friend)
