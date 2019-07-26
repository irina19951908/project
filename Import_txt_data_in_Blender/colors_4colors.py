import bpy


from bpy.props import *
from mathutils import Color


# because python does not know Clamp
def Clamp(val, clampMin, clampMax):
    return max(min(val, clampMax), clampMin)

bpy.types.Object.my_denominator1 = FloatProperty(name = "", default = 0.3, min = 0.001, max = 1)
    
bpy.types.Object.my_denominator2 = FloatProperty(
    name = "", default = 0.6, 
    min = 0.001, max = 1)
    
bpy.types.Object.my_denominator3 = FloatProperty(
    name = "", default = 0.9, 
    min = 0.001, max = 1)
    


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Materials"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object

        row = layout.row()
        #row.label(text="Colorbar", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        
        row = layout.row()
        #row.operator("mesh.primitive_cube_add")
        row = layout.row()
        #layout.prop(obj, "my_denominator1")
        layout.prop(obj, 'my_denominator1')
        layout.prop(obj, "my_denominator2")
        layout.prop(obj, "my_denominator3")
        row = layout.row()
        row.operator("panel.color")
        
        #    Установка кнопки
class OBJECT_OT_SetButton(bpy.types.Operator):
    bl_idname = "panel.color"
    bl_label = "Set color"

    def execute(self, context):
        scn = context.scene
        global theSwatches
        ob = context.object.data
        obj = context.object

        #ob = obj.data
        topPoint = ob.vertices[0].co + obj.location
        botPoint = ob.vertices[0].co + obj.location
        for vertex in ob.vertices:
            vert = vertex.co
            if(vert.z + obj.location.z > topPoint.z):
                topPoint = vert + obj.location
            if(vert.z + obj.location.z < botPoint.z):
                botPoint = vert + obj.location
                
        min = ob.vertices[0].co.z
        max = ob.vertices[0].co.z
        for vertex in ob.vertices:
            vert = vertex.co
            if (vert.z < min):
                min = vert.z
                
        for vertex in ob.vertices:
            vert = vertex.co
            if (vert.z > max):
                max = vert.z
                
        BorderMinZ, BorderMaxZ = min, max # границы раскраски
        R = abs(BorderMinZ)+abs(BorderMaxZ)
        #mat = bpy.data.materials.new('newMat')
        #ob.materials.append(mat)
        color_map_collection = ob.vertex_colors
        if len(color_map_collection) == 0:
            color_map_collection.new()
        color_map = color_map_collection['Col']
        vCol = ob.vertex_colors['Col'].data
        i = 0
            #for poly in ob.polygons:
            #    for idx in poly.loop_indices:
            #        rgb = (1,0,0)
            #        color_map.data[i].color = rgb
            #        i += 1
        cursorLocation = bpy.context.scene.cursor_location
        '''if(parameter == 'BOT'):
            botPoint = cursorLocation
        if( parameter == 'TOP'):
            topPoint = cursorLocation'''
        #botPoint = cursorLocation
        #topPoint = cursorLocation
        col_normalMod = 0
        for poly in ob.polygons:
            for idx in poly.loop_indices:
                vertIDInLoop = ob.loops[idx-1].vertex_index
                vertCol = vCol[idx]
                vertexCoords = ob.vertices[vertIDInLoop-1].co
                if (vertexCoords.z >= BorderMinZ) and (vertexCoords.z <= BorderMinZ+R*0.12):
                    vertCol.color = Color((0.093, 0.105, 0.8))
                    #color_map.data[i].color = (0.093, 0.105, 0.8)
                elif (vertexCoords.z >= BorderMinZ+R*0.12) and (vertexCoords.z <= BorderMinZ+R*0.3):
                    vertCol.color = Color((0.139, 0.8, 0.140))
                    #color_map.data[i].color = (0.139, 0.8, 0.140)
                elif (vertexCoords.z >= BorderMinZ+R*0.3) and (vertexCoords.z <= BorderMinZ+R*0.75):
                    vertCol.color = Color((0.8, 0.744, 0.074))
                    #color_map.data[i].color = (0.8, 0.744, 0.074)
                else:
                    vertCol.color = Color((0.8, 0.077, 0.87))
                    #color_map.data[i].color = (0.8, 0.077, 0.87)
            

        
        mat = bpy.data.materials.new('vertex_material')
        mat.use_vertex_color_paint = True
        mat.use_vertex_color_light = True  # material affected by lights

        ob.materials.append(mat)
        return{'FINISHED'}

bpy.utils.register_module(__name__)
# Регистрация
#bpy.utils.register_class(HelloWorldPanel)

