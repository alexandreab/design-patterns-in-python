from component import Component

'''
Hierarchy:
Saul
    Alex
    Alice
        Bob
            Carlos
    Amy
        Bella
        Brooke
    Abigail
        Brandon
            Caleb
                Daniel
                    Evelyn
                        Freya
                        Faye
'''

# Declare components
faye = Component('Faye')
freya = Component('Freya')
evelyn = Component('Evelyn')
daniel = Component('Daniel')
caleb = Component('Caleb')
brandon = Component('Brandon')
abigail = Component('Abigail')
brooke = Component('Brooke')
bella = Component('Bella')
amy = Component('Amy')
carlos = Component('Carlos')
bob = Component('Bob')
alice = Component('Alice')
alex = Component('Alex')
saul = Component('Saul')

# Create hierarchy
evelyn.add_children([freya, faye])
daniel.add_child(evelyn)
caleb.add_child(daniel)
brandon.add_child(caleb)
abigail.add_child(brandon)
amy.add_children([bella, brooke])
bob.add_child(carlos)
alice.add_child(bob)
saul.add_children([alex, alice, amy, abigail])


# call a method that will be called for all children

saul.greet('Jake')
