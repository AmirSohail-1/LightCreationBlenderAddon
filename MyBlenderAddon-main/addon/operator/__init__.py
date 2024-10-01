import bpy

from .add_lights import GEM_OP_Add_Lights

# Tupple need , bcoz other wise it will take as parameter bracket
classes = (
    GEM_OP_Add_Lights,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)