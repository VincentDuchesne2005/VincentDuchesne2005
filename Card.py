class Card:

    #Take in a value from 1-13 and a suite
    def __init__(self, v, s):
        self.value = v
        self.suite = s

    def get_value(self):
        return self.value

    def get_suite(self):
        return self.suite