class Point(object):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def get_coordinates(self) -> (float, float):
        return self.x, self.y

    def set_coordinates(self, new_x: float, new_y: float) -> None:
        assert (isinstance(new_x, (float, int)) and isinstance(new_y, (float, int)))
        self.x = new_x
        self.y = new_y

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Point(x=self.x*other, y=self.y*other)
        else:
            raise ValueError("Unknown object for multiplication with <Point>")

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return Point(x=self.x/other, y=self.y/other)

    def __str__(self) -> str:
        return f"{self.x} {self.y}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x},{self.y})"


class MaterialPoint(object):
    def __init__(self, x: float, y: float, char="*") -> None:
        self.coordinates = Point(x, y)
        self.char = char

    def get_data(self) -> (Point, str):
        return self.coordinates, self.char

    def move_to(self, new_x: float, new_y: float) -> None:
        self.coordinates.set_coordinates(new_x, new_y)


class World(object):
    def __init__(self, camera_pos: Point) -> None:
        self.camera_pos = camera_pos
        self.objects = dict()

    def get_world_info(self) -> None:
        log = "\n"
        log += f"Number of objects: {len(self.objects)}\n"
        log += f"Camera position: {self.camera_pos}\n"
        print(log)

    def get_objects(self) -> dict:
        return self.objects

    def add_object(self, obj):
        self.objects[f"{obj.name}-{obj.id}"] = obj
