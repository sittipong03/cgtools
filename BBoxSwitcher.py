import maya.cmds as cmds
import sys

selectobj = cmds.ls(sl=True)
selected = cmds.listRelatives(selectobj , ad =True, type = "transform")
for y in selectobj:
    selected.append(y)
overrideObj = []

for i in selected:
    currentValue = cmds.getAttr(i + ".overrideEnabled")
    if (currentValue) == True:
        overrideObj.append(i)
    else:
        pass
        
if len(overrideObj) >= 1:
    for z in overrideObj:
        cmds.setAttr (z + ".overrideEnabled", 0)
        cmds.setAttr (z + ".overrideLevelOfDetail", 1)
        sys.stdout.write("Bounding Box: OFF\n")
elif len(overrideObj) == 0:
    for u in selectobj:
        cmds.setAttr (u + ".overrideEnabled", 1)
        cmds.setAttr (u + ".overrideLevelOfDetail", 1)
        sys.stdout.write("Bounding Box: ON\n") 
        
