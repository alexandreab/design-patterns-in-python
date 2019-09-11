class Component:
    def __init__(self, name, children=None):
        if not children:
            children = list()

        for child in children:
            if not isinstance(child, Component):
                raise ValueError("Every added child must be a component"
                                 " object.")
        self.name = name
        self.children = children

    def add_child(self, child):
        if not isinstance(child, Component):
            raise ValueError("The added child must be a component object.")
        self.children.append(child)

    def add_children(self, children):
        for child in children:
            if not isinstance(child, Component):
                raise ValueError("Every added child must be a component"
                                 " object.")
        self.children += children

    def greet(self, name):
        children_count = len(self.children)
        print(f"Object id {id(self)} - Hi, {name}! I'm {self.name}. "
              f"I have {children_count} children. "
              "They will greet you, too. :)")
        for child in self.children:
            child.greet(name)
