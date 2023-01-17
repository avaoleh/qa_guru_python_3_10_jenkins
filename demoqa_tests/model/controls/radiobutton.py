from selene import have


class Radiobutton:
    def __init__(self, element):
        self.element = element

    def select_by_value(self, text):
        self.element.element_by(have.value(text)).element('..').click()
