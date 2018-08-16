
bl_info = {
    "name": "contino",
    "author": "Alisseo",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "View3D > Tools > Mesh Contino",
    "description": "Mesh counter",
    "category": "Mesh Tool",
    }

import bpy


objects = bpy.context.scene.objects
list=[]
for obj in objects:
    list.append(obj.name)           
print(list)



class contino_panel(bpy.types.Panel):
    """Mesh Contino"""
    bl_label = "Mesh Contino"
    bl_idname = "OBJECT_PT_select"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Mesh Ccontino"
    
    def draw(self, context):
        layout = self.layout
        
        row_1 = layout.row()
        row_1.label(text="Selected Objects:") 
                

        
def register():

def unregister():

if __name__ == "__main__":
register()
