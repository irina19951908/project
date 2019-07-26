import bpy
import array
import os
import time
import bpy
import mathutils
import math
import random





# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy_extras.io_utils import unpack_list
from bpy_extras.image_utils import load_image
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from mathutils import Color
bl_info = {
    'name': 'Import_txt',
    'blender': (2, 7, 6),
    'location': 'File > Import > TXT',
    'description': 'Import files in format (.txt)',
    'category': 'Import-Export'
}


# because python does not know Clamp
def Clamp(val, clampMin, clampMax):
    return max(min(val, clampMax), clampMin)

            
class ImportTXT(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Some Data"

    # ImportHelper mixin class uses this
    filename_ext = ".txt"

    filter_glob = StringProperty(
            default="*.txt",
            options={'HIDDEN'},
            )
     #List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting = BoolProperty(
            name="Example Boolean",
            description="Example Tooltip",
            default=True,
            )

    type = EnumProperty(
            name="Example Enum",
            description="Choose between two items",
            items=(('OPT_A', "First Option", "Description one"),
                   ('OPT_B', "Second Option", "Description two")),
            default='OPT_A',
            )



    
    def execute(self, context):
            f = open(self.filepath, 'r', encoding='utf-8')
            verts = []
            edges = []
            faces = []
            ring1 = []
            ring2 = []
            ring3 = []
            ring4 = []
            #N = []
            #M = []
            
       
            
            for line in f.read().split("\n"):
                verts.append(list(map(lambda x: float(x), line.split("\t"))))
            
            #N = int(verts[0][0])
            #M = int(verts[0][1])
            #del verts[0]
            
            f.close()
            
            #kol Y
            m=0
            for i in range(len(verts)-1):
                m=m+1
                if verts[i][0] != verts[i+1][0]:
                    break
             
            #kol X
            n=1    
            for i in range(len(verts)-1):
                if verts[i][0] != verts[i+1][0]:
                    n=n+1

                            
            max = verts[0][2]
            min = verts[0][2]
            for i in range(len(verts)-1):
                if verts[i][2] > max:
                    max = verts[i][2]
                    
            for i in range(len(verts)-1):
                if verts[i][2] < min:
                    min = verts[i][2]
            
            a = 0
            b = 0
            c = 0
            d = 0
        
            for i in range(n-1):
                for j in range(m-1):
                    a = i*m+j
                    b = i*m+j+1
                    c = i*m+j+m
                    d = i*m+j+m+1
                    faces.append([a,b,d,c])        
            
            
            # Create material


            

                
            

                            
            
                
            VertsMesh = bpy.data.meshes.new("Verts")

            VertsMesh.from_pydata(verts, edges, faces)
            VertsMesh.update()
            mesh = bpy.data.objects.new("Verts", VertsMesh)  
            
            #mat1 = bpy.data.materials.new('Red')
            #mat2 = bpy.data.materials.new('Green')
            #mat3 = bpy.data.materials.new('Blue')
            #mat1.diffuse_color = (1,0,0)
            #mat2.diffuse_color = (0,1,0)
            #mat3.diffuse_color = (0,0,1)
            #mat.diffuse_color = (1,0,0)
            
            #for i in range(len(verts)-1):
            #    if (verts[i][2] > 0.66) and (verts[i][2] <= 1):
            #        ob.materials.append(mat1)
            #    if (verts[i][2] >= 0.33) and (verts[i][2] <= 0.66):
            #        ob.materials.append(mat2)
            #    if (verts[i][2] >= 0) and (verts[i][2] < 0.33):
            #        ob.materials.append(mat3)
            #ob.materials.append(mat)
            
            #ob = mesh.data
            #while len(ob.materials) < 3:
            #    mat = bpy.data.materials.new('newMat')
            #    ob.materials.append(mat)
            #ob.materials[0].diffuse_color = (1, 0, 0)
            #ob.materials[1].diffuse_color = (0, 1, 0)
            #ob.materials[2].diffuse_color = (0, 0, 1)
            
            
            bpy.context.scene.objects.link(mesh)
            bpy.ops.object.select_all(action="DESELECT")
            #bpy.ops.object.mode_set(mode='VERTEX_PAINT')
            mesh.select = True
            bpy.context.scene.objects.active = mesh

            
            
    

            return {'FINISHED'}

# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(ImportSomeData.bl_idname, text="Text Import Operator")


def register():
    bpy.utils.register_class(ImportTXT)
    bpy.types.INFO_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportTXT)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
