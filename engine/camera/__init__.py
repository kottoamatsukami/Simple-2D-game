import engine.utils


class Camera(object):
    def __init__(self, start_x=0, start_y=0, width=160, height=90) -> None:
        self.coords = engine.utils.Point(x=start_x, y=start_y)
        self.width = width
        self.height = height
        self.void_char = " "
        self.screen = [[self.void_char for _ in range(self.width)] for _ in range(self.height)]

    def clear_screen(self) -> None:
        self.screen = [[self.void_char for _ in range(self.width)] for _ in range(self.height)]

    def render(self) -> None:
        for row in self.screen:
            for char in row:
                print(char, end="")
            print()

    def move_to(self, new_x: float, new_y: float) -> None:
        self.coords.set_coordinates(new_x, new_y)

    def get_coords(self) -> engine.utils.Point:
        return self.coords
