class Button:

    def __init__(self, x, y, horizontal, vertical):
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.vertical = vertical

    def isOn(self, xmouse, ymouse):
        if self.x <= xmouse <= self.x + self.horizontal and self.y <= ymouse <= self.y + self.vertical:
            return True
        return False