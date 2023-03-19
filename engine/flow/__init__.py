import engine.camera
import engine.utils


class WorldManager(object):
    def __init__(self, world_list: dict) -> None:
        """
        world_list = {
            "<world_1_name>" : object,
            ...
            "<world_n_name>" : object,
        }
        """
        self.world_list = world_list

    def get_world(self, world_name: str) -> engine.utils.World:
        return self.world_list[world_name]

    def add_world(self, world_name: str, world: engine.utils.World) -> None:
        self.world_list[world_name] = world

    def remove_world(self, world_name: str) -> None:
        self.world_list.pop(world_name)

    def __len__(self) -> int:
        return len(self.world_list)


class GameShell(object):
    def __init__(self, world_manager: WorldManager, camera: engine.camera.Camera) -> None:
        self.world_manager = world_manager
        self.camera = camera
        self.curr_world = None

    def link(self, world_name: str) -> None:
        assert len(self.world_manager) > 0
        self.curr_world = self.world_manager.get_world(world_name=world_name)
        self.curr_world.camera_pos = self.camera.get_coords()

    def start(self):
        while True:
