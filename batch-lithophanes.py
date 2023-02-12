import lithophane_utils as lu

import lithophane_image as li
import scale
import import_image
import create_tube
import os

src_folder = os.path.abspath("C:\\Users\\jonathan\\Work\\Programming\\lightsaber\\image-adjustment\\equalized")

def generate_lithophane(img):
    #create image
    path = os.path.join(src_folder, img)
    li.createImage(path)

    #select image
    FreeCADGui.Selection.addSelection('Unnamed','_')

    #create tube
    tube = create_tube.CreateTubeCommand()
    tube.Activated()

    #scale to diameter
    (image, label, freeCadObject) = lu.findSelectedImage(includeObject=True)
    panel = scale.ScalePanel(image, freeCadObject)

    newPerimeter = lu.perimeterFromDiameter(28.5)
    panel.updateScaleFactor(panel.originalLength, newPerimeter)
    panel.updateValues()
    panel.accept()

    #export to src_folder
    __objs__=[]
    __objs__.append(FreeCAD.getDocument("Unnamed").getObject("__Result"))
    import Mesh
    Mesh.export(__objs__, path +"_litho.stl") 
    del __objs__

    #delete objects
    App.getDocument('Unnamed').removeObject('__Result')
    App.getDocument('Unnamed').removeObject('_')
    App.getDocument('Unnamed').removeObject('__Mesh')

for filename in os.listdir(src_folder):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        generate_lithophane(filename)

print("lithophane generation complete.")