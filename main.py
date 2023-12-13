class ColorIterator:
    def __init__(self, colors):
        self.colors = colors
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.colors:  
            raise StopIteration

        color = self.colors[self.index]
        self.index = (self.index + 1) % len(self.colors)  
        return color

colors = ["red", "green", "blue", "yellow"]

color_iterator = ColorIterator(colors)

for _ in range(10):
    print(next(color_iterator))
