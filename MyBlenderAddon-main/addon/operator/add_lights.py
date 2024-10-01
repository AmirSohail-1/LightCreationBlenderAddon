import bpy


class GEM_OP_Add_Lights(bpy.types.Operator):
    """Adds lights to the scene."""

    bl_idname = "gem.add_lights"
    bl_label = "Add Lights"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        print("HERE")
        return {'FINISHED'}