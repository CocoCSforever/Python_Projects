from person import Person


def main():
    person1 = Person("Marge Simpson", 32)
    person2 = Person("Asterix the Gaul", 55)
    another_party_guest = Person("Leia Organa", 29)
    # guest = Person("Joe"): missing 1 required positional argument
    # unless we have an optional argument

    person2.introduce_self()
    person1.introduce_self()
    another_party_guest.introduce_self()

    person1.befriend(person2)
    person1.befriend(another_party_guest)

    person1.introduce_self()
    person2.introduce_self()


if __name__ == "__main__":
    main()
