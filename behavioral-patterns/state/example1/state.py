class Context:
    def __init__(self, inital_state=None):
        if not inital_state:
            inital_state = NeutralState()
        self._state = inital_state
        self._points = 1

    def give_input(self, text_input):
        if text_input == 'give_food':
            self._state = HappyState()
        elif text_input == 'do_nothing':
            self._state = NeutralState()
        else:
            self._state = SadState()

        self.update_points()

    def update_points(self):
        self._points = self._state.calculate_reward(self._points)

    def get_points(self):
        return self._points


class State:
    def __init__(self):
        raise NotImplementedError("State base class can not be instantiated")

    def calculate_reward(self, value):
        return self._base_reward * value


class HappyState(State):
    def __init__(self):
        self._base_reward = 2


class NeutralState(State):
    def __init__(self):
        self._base_reward = 1


class SadState(State):
    def __init__(self):
        self._base_reward = 0.5
