import bpy
import array
import os
import time
import bpy
import mathutils
import math
import numpy as np
import random
import cProfile
import pstats
import io



# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from bpy.props import *
from mathutils import Color
#from math import asin,tan,pi,radians

#cProfile.run("import bpy; bpy.utils.load_scripts()","blender.prof")
#p=pstats.Stats("blender.prof")
#p.sort_stats("cumulative").print_stats(20)

Output="C://Users//User//Desktop//status.txt"

bl_info = {
    'name': 'Import_bin',
    'blender': (2, 7, 9),
    'location': 'File > Import > .bin',
    'category': 'Import-Export'
}


def frame(camera,x,y,z,mat,step_transparency):
    '''maxx = max(v.x for v in bb) #минимальный и максимальный размер габаритного ящика
    maxy = max(v.y for v in bb)
    maxz = max(v.z for v in bb)
    minx = min(v.x for v in bb)
    miny = min(v.y for v in bb)
    minz = min(v.z for v in bb)'''
    '''wx=maxx-minx #вычисления ширины
    wy=maxy-miny
    wz=maxz-minz
    m=Mathutils.Vector((wx/2.0,wy/2.0,wz/2.0)) #допускаем, что наш предмет отцентрирован в начале координат
    maxw=max((wx,wy,wz))/2.0 #самая большая ширина из всех осей'''
    #sins=[]
    #p=camera.location#Mathutils.Vector(Object.Get(camera).getLocation('worldspace'))
    x1=camera.location[0]-x
    y1=camera.location[1]-y
    z1=camera.location[2]-z
    d=math.fabs(math.sqrt(x1*x1+y1*y1+z1*z1))#расстояние d до средней точки габаритного ящика
    
    if (d < 3):
        mat.use_transparency = True
        mat.alpha = 1 - step_transparency
        
        #sins.append(maxw/d)
    #mat.use_transparency = True
    #mat.alpha = 0.1 #прозрачность

class ImportSomeData(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Some Data"

    # ImportHelper mixin class uses this
    filename_ext = ".bin"

    filter_glob = StringProperty(
            default="*.bin",
            options={'HIDDEN'},
            maxlen=255,  # Max internal buffer length, longer would be clamped.
            )

    # List of operator properties, the attributes will be assigned
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
        #статистика
        '''pr=cProfile.Profile()
        pr.enable()'''
        
        file = open(self.filepath,"rb")
        #выбор камеры
        #cam_ob = bpy.data.cameras["Camera"]
        cam_ob = bpy.data.objects['Camera']
        #cam_ob.clip_start = 10
        #f = open(self.filepath, 'r', encoding='utf-8') #чтение выбранного файла
        #вершины
        mat = [] #материалы
        
        N = np.fromfile(file,np.int32,1)
        Nreal = np.fromfile(file,np.int32,1)
        dt = np.fromfile(file,np.float64,1)
        t = np.fromfile(file,np.float64,1)
        x = np.fromfile(file,np.float64,int(N))
        y = np.fromfile(file,np.float64,int(N))
        z = np.fromfile(file,np.float64,int(N))
        U = np.fromfile(file,np.float64,int(N))
        V = np.fromfile(file,np.float64,int(N))
        W = np.fromfile(file,np.float64,int(N))
        E = np.fromfile(file,np.float64,int(N))
        Rho = np.fromfile(file,np.float64,int(N))
        P = np.fromfile(file,np.float64,int(N))
        verts = np.zeros((N,3)) 
        for i in range(N):
            verts[i][0]=x[i];
            verts[i][1]= y[i];
            verts[i][2]= z[i];

        H = np.zeros(N)
        step = 0.001
        for i in range(N):
            H[i] = 0.01 + step
            step += 0.00001
        ColRed = max(Rho)
        ColBlue = min(Rho)
        step_transparency = 0#шаг для прозрачности частицы
        for i in range(N):#1 слой
            if(verts[i][2]>=0 and verts[i][2]<=0.1):
                '''if(P[i]<0.01):
                    bpy.ops.mesh.primitive_uv_sphere_add(size=P[i],location=(verts[i][0],verts[i][1],verts[i][2]))
                else:
                    bpy.ops.mesh.primitive_uv_sphere_add(size=0.01,location=(verts[i][0],verts[i][1],verts[i][2]))'''
                bpy.ops.mesh.primitive_uv_sphere_add(size=(H[i]),location=(verts[i][0],verts[i][1],verts[i][2]))
                ob = bpy.context.object.data
                mat = bpy.data.materials.new('newMat')
                
                
                mat.diffuse_color = (ColRed, 0, ColBlue)
                '''if(Rho[i]<max(Rho/3)):
                    mat.diffuse_color = (0, 0, Rho[i])
                if(Rho[i]>=max(Rho/3) and Rho[i]<max(2*Rho/3)):
                    mat.diffuse_color = (Rho[i], 0, 0)
                if(Rho[i]>max(2*Rho/3)):
                    mat.diffuse_color = (Rho[i], 0, 0)'''
                #mat.use_transparency = True
                #mat.alpha = 0.1 #прозрачность
                #ob = bpy.context.object
                frame(cam_ob,verts[i][0],verts[i][1],verts[i][2],mat,step_transparency)
                ob.materials.append(mat)
                ColBlue = ColBlue + 0.001#Rho[i]/max(Rho)#max(Rho)/Rho[i]
                ColRed = ColRed -0.001#/Rho[i]#Rho[i]/max(Rho)
                step_transparency += 0.001
            
            '''if(P[i]<max(P/3)):
                mat.diffuse_color = (0, 0, P[i]*10)
            if(P[i]>=max(P/3) and P[i]<max(2*P/3)):
                mat.diffuse_color = (P[i]*10, 0, P[i]*10)
            if(P[i]>max(2*P/3)):
                mat.diffuse_color = (P[i]*10, 0, 0)'''
            
            
        
            
        #bpy.ops.mesh.primitive_uv_sphere_add(size=0.01,location=(verts[1][0],verts[1][1],verts[1][2]))  
        
        #VertsMesh = bpy.data.meshes.new("NewObject")

        #VertsMesh.from_pydata(verts, [], [])
        #VertsMesh.update()
        #mesh = bpy.data.objects.new("NewObject", VertsMesh)

        #bpy.context.scene.objects.link(mesh) 
        #bpy.ops.object.select_all(action="DESELECT")
        #mesh.select = True
        #bpy.context.scene.objects.active = mesh
        
        #статистика 
        '''pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr,stream=s).sort_stats(sortby)
        ps.print_stats()
        #open and write to file
        binfile = open(Output,'w')
        binfile.write(s.getvalue())
        binfile.close()'''
        return {'FINISHED'}



# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(ImportSomeData.bl_idname, text="Text Import Operator")


def register():
    bpy.utils.register_class(ImportSomeData)
    bpy.types.INFO_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportSomeData)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_test.some_data('INVOKE_DEFAULT')
