
import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
def system_movement(world:esper.World,delta_time:float):
    compoments = world.get_components(CTransform,CVelocity)
    c_t:CTransform
    c_s:CVelocity
    for entity, (c_t,c_v) in compoments:
        c_t.pos.x += c_v.vel.x * delta_time
        c_t.pos.y += c_v.vel.y * delta_time
