import maya.cmds as cmds

#arnold section

def selectANObj():
    # function list aiStandIn from select obj
    selectANSI = []
    getSelect = cmds.ls(sl = True , type = 'transform')
    for i in getSelect:
        connectedMesh = cmds.listRelatives(i ,ad = True ,type = 'aiStandIn')
        selectANSI.append(str(connectedMesh[0]))       
    return selectANSI

def allANObj():
    # function that list all aiStandIn in scene
    selectANSI = []
    getSelect = cmds.ls(type = 'aiStandIn')
    for i in getSelect:
        selectANSI.append(str(i))
    return selectANSI

def setaiStandinDisplay(*agr):
    # set attribute function

    # get value from main window
    anSelectObj = cmds.radioButton('anSelectObj' , query = True , select = True)
    allaiStandin = cmds.radioButton('allaiStandin' , query = True , select = True)
    anPreviewMesh = cmds.radioButton('anPreviewMesh' , query = True , select = True)
    anWireframe = cmds.radioButton('anWireframe' , query = True , select = True)
    anBoundingBox = cmds.radioButton('anBoundingBox' , query = True , select = True)

    # check conditions and set attribute 
    if anPreviewMesh == True:
        if anSelectObj == True:
            selectedObj = selectANObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".mode" ,6)
        elif allaiStandin == True:
            selectedObj = allANObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".mode" ,6)

    elif anBoundingBox == True:
        if anSelectObj == True:
            selectedObj = selectANObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".mode" ,0)
        elif allaiStandin == True:
            selectedObj = allANObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".mode" ,0)

    elif anWireframe == True:
        if anSelectObj == True:
            selectedObj = selectANObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".mode" ,3)
        elif allaiStandin == True:
            selectedObj = allANObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".mode" ,3)
    
    
#redshift section

def selectRSObj():
    # function list redshift proxy from select obj
    selectRSPX = []
    getSelect = cmds.ls(sl = True , type = 'transform')
    for i in getSelect:
        connectedMesh = cmds.listRelatives(i ,ad = True ,type = 'mesh') # list obj under selected mesh node (rsproxy will connect to mesh)
        if connectedMesh != None: # check is there rspx under mesh node
            rspxObj = cmds.listConnections(connectedMesh , type = 'RedshiftProxyMesh') # list obj under mesh node must be rspx node
            selectRSPX.append(str(rspxObj[0]))
    return selectRSPX
def allRSObj():
    # function that list all redshift proxy in scene
    selectRSPX = []
    getSelect = cmds.ls(type = 'RedshiftProxyMesh')
    for i in getSelect:
        selectRSPX.append(str(i))
    return selectRSPX
def setRsProxyDisplay(*agr):
    # set attribute function

    # get value from main window
    rsSelectObj = cmds.radioButton('rsSelectObj' , query = True , select = True)
    allRSProxy = cmds.radioButton('allRSProxy' , query = True , select = True)
    rsPreviewMesh = cmds.radioButton('rsPreviewMesh' , query = True , select = True)
    rsBoundingBox = cmds.radioButton('rsBoundingBox' , query = True , select = True)
    rsDisplayPercentage = cmds.textFieldGrp( 'rsDisplayPercentage' , query = True , text = True )

    # check conditions and set attribute 
    if rsPreviewMesh == True:
        if rsSelectObj == True:
            selectedObj = selectRSObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".displayMode" ,1)
                cmds.setAttr(obj + ".displayPercent" ,int(rsDisplayPercentage))
        elif allRSProxy == True:
            selectedObj = allRSObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".displayMode" ,1)
                cmds.setAttr(obj + ".displayPercent" ,int(rsDisplayPercentage))

    elif rsBoundingBox == True:
        if rsSelectObj == True:
            selectedObj = selectRSObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".displayMode" ,0)
        elif allRSProxy == True:
            selectedObj = allRSObj()
            for obj in selectedObj:
                cmds.setAttr(obj + ".displayMode" ,0)

def main():
    #####################################################################################################
    #
    #
    # create main window
    #
    # each section will parent with their columm/row layout
    # 
    #
    #####################################################################################################
    if cmds.window('Proxy Display control', exists=True):
        cmds.deleteUI('Proxy Display control')
    nzt_Tools = cmds.window('Proxy Display control', title='Proxy Display control', iconName='Short Name', widthHeight=(200,55), resizeToFitChildren=True)
    
    #create main tab layout
    mainTab = cmds.shelfTabLayout( 'mainShelfTab' ,p = nzt_Tools )
        
    #arnold section
    
    #arnold tab layout parent with main tab (it can attach layout to tab layout)
    arnoldTab = cmds.columnLayout('Arnold' , parent=mainTab, columnAttach=('both', 5), adjustableColumn = True )
    
    #first row select mode ,how to select obj allobj or selected obj
    arFirstRow = cmds.rowColumnLayout(parent = arnoldTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.text(parent = arFirstRow, label = "Select Mode", align = 'center', height = 20 , width = 100) 
    cmds.radioCollection()
    anSelectObj = cmds.radioButton( 'anSelectObj' , parent = arFirstRow, label='select Object' ,select = True)
    allaiStandin = cmds.radioButton( 'allaiStandin' , parent = arFirstRow, label='all aiStandin' )
    
    #Second row display mode there are 3 mode mesh, wireframe , bounding box   
    arSecondRow = cmds.rowColumnLayout(parent = arnoldTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.text(parent = arSecondRow, label = "Disply Mode", align = 'center', height = 20 , width = 100)
    cmds.radioCollection()
    anPreviewMesh = cmds.radioButton( 'anPreviewMesh' ,parent = arSecondRow, label='Preview Mesh' ,select = True )
    anWireframe = cmds.radioButton( 'anWireframe' ,parent = arSecondRow, label='Wireframe' )
    anBoundingBox = cmds.radioButton( 'anBoundingBox' ,parent = arSecondRow, label='Bounding Box' )
    cmds.separator(parent = arnoldTab ,width = 80, height = 10, style = "none")
    
    #Third row submit button       
    arThirdRow = cmds.rowColumnLayout(parent = arnoldTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.button(parent = arThirdRow, label = "Apply", command = "setaiStandinDisplay()" , height = 20 , width = 400)
    cmds.separator(parent = arnoldTab ,width = 80, height = 10, style = "none")
    
       
    #redshift section
    
    #redshift tab layout parent with main tab (it can attach layout to tab layout)
    redshiftTab = cmds.columnLayout('Redshift' ,  parent=mainTab, columnAttach=('both', 5), adjustableColumn = True )
    
    #first row select mode ,how to select obj allobj or selected obj
    rsFirstRow = cmds.rowColumnLayout(parent = redshiftTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.text(parent = rsFirstRow, label = "Select Mode", align = 'center', height = 20 , width = 100)
    cmds.radioCollection()
    rsSelectObj = cmds.radioButton( 'rsSelectObj' , parent = rsFirstRow, label='select Object' ,select = True)
    allRSProxy = cmds.radioButton( 'allRSProxy' , parent = rsFirstRow, label='all RSProxy' )
    
    #Second row display mode there are 2 mode mesh, bounding box   
    rsSecondRow = cmds.rowColumnLayout(parent = redshiftTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.text(parent = rsSecondRow, label = "Disply Mode", align = 'center', height = 20 , width = 100)
    cmds.radioCollection()
    rsPreviewMesh = cmds.radioButton( 'rsPreviewMesh' ,parent = rsSecondRow, label='Preview Mesh' ,select = True )
    rsBoundingBox = cmds.radioButton( 'rsBoundingBox' ,parent = rsSecondRow, label='Bounding Box' )
    
    #Third row display Percentage         
    rsThirdRow = cmds.rowColumnLayout(parent = redshiftTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.text(parent = rsThirdRow, label = "Display Percentage" , align = 'center', height = 20 , width = 100)
    rsDisplayPercentage = cmds.textFieldGrp( 'rsDisplayPercentage' , parent = rsThirdRow, text='80' )
    cmds.separator(parent = redshiftTab ,width = 80, height = 10, style = "none")
    
    #Forth row submit button       
    rsForthRow = cmds.rowColumnLayout(parent = redshiftTab, numberOfRows = 1, columnSpacing = (1, 10) )
    cmds.button(parent = rsForthRow, label = "Apply", command = "setRsProxyDisplay()" , height = 20 , width = 400)
    cmds.separator(parent = redshiftTab ,width = 80, height = 10, style = "none") 
        
        
    cmds.showWindow(nzt_Tools)
main()
