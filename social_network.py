
class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend == self:
            print("A person cannot be friends with themselves.")
            return

        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
            return

        person = Person(name)
        self.people[name] = person

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        if person1 == person2:
            print("A person cannot be friends with themselves.")
            return

        if person2 in person1.friends:
            print("These people are already friends!")
            return

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]

            if friend_names:
                print(f"{name} is friends with: {', '.join(friend_names)}")
            else:
                print(f"{name} has no friends yet.")


# Test the social network

network = SocialNetwork()

# Add at least six people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate person
network.add_person("Alex")

# Create at least eight friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Test friendship with a person who doesn't exist
network.add_friendship("Alex", "Johnny")

# Test duplicate friendship
network.add_friendship("Alex", "Jordan")

# Print the completed network
print("\nSOCIAL NETWORK:")
network.print_network()


# DESIGN MEMO
#
# A graph is the best data structure for representing a social network
# because people can connect with multiple people in different ways.
# Each person represents a node, and each friendship represents an
# edge connecting two nodes. Since friendships are bidirectional,
# both people need to store each other in their friends lists.
#
# A list would not work as well because it does not naturally represent
# relationships between multiple people. Finding connections would
# require searching through the list. A tree would also be less
# appropriate because trees usually follow a parent-child structure.
# Social networks do not have one central parent or a strict hierarchy.
# People can have many friendships without following a particular order.
#
# Using an adjacency list makes this network efficient and flexible.
# Adding a person to the dictionary takes approximately O(1) time on
# average. Adding a friendship requires checking whether the two people
# exist and whether they are already connected. Checking a person's
# friends list takes O(d) time, where d is that person's number of
# friends. Printing the network takes O(V + E) time because the program
# visits every person and displays their connections.
#
# One trade-off is that storing friendships in both people's lists
# requires additional memory. However, this makes friendships easier
# to access in either direction. Overall, an adjacency list provides
# a practical way to manage a growing social network.
