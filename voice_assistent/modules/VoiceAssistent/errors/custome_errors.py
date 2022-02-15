class DidNotUnderstand(Exception):
    def __str__(self):
        return "Didn't understand what you said"


class CannotOpenApplication(Exception):
    def __str__(self):
        return "Couldn't open specified application"
