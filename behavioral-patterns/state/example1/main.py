from state import Context

if __name__ == '__main__':
    tamagoshi = Context()
    # It'll print 1
    print("Initial points:", tamagoshi.get_points())

    tamagoshi.give_input('give_food')
    # It'll print 2
    print("Points after give food one time:", tamagoshi.get_points())

    tamagoshi.give_input('give_food')
    tamagoshi.give_input('give_food')
    # It'll print 8
    print("Points after give food two times:", tamagoshi.get_points())

    tamagoshi.give_input('make_face')
    # It'll print 4
    print("Points after make face:", tamagoshi.get_points())

    tamagoshi.give_input('do_nothing')
    # It'll print 4
    print("Points after do nothing:", tamagoshi.get_points())
