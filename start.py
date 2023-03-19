import engine.utils
import engine.camera
import engine.flow


world_manager = engine.flow.WorldManager(
    world_list={
        "null_world": engine.utils.World(
                    camera_pos=engine.utils.Point(
                        x=0,
                        y=0,
                        ),
                    ),
    }
)

camera = engine.camera.Camera(
    start_x=0,
    start_y=0,
    width=160,
    height=90,
)

kernel = engine.flow.GameShell(
    world_manager=world_manager,
    camera=camera,
)
kernel.link(
    world_name="null_world"
)

kernel.start()