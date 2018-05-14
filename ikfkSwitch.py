import maya.cmds as cmds
import json

RIG_DATA = dict()

def getCharData():
    global RIG_DATA
    with open("Z:\maya\scripts\python\ikfkSwitch\ikfkSwitch.cfg", 'r') as fd:
        RIG_DATA = json.load(fd)

def fkToIkDef(ikJnt01,ikJnt02,ikJnt03,fkCtrl01,fkCtrl02,fkCtrl03):
    #match FK to IK, change IK Handle wherever you want then run
    #ikJnt01, ikJnt02, ikJnt03, fkCtrl01, fkCtrl02, fkCtrl03
    
    qIkJntRot01 = cmds.xform( ikJnt01, query=True, worldSpace = True, rotation = True )
    cmds.xform(fkCtrl01,rotation = (qIkJntRot01[0],qIkJntRot01[1],qIkJntRot01[2]),worldSpace = True)
    
    qIkJntRot02 = cmds.xform( ikJnt02, query=True, worldSpace = True, rotation = True )
    cmds.xform(fkCtrl02,rotation = (qIkJntRot02[0],qIkJntRot02[1],qIkJntRot02[2]),worldSpace = True)
    
    qIkJntRot03 = cmds.xform( ikJnt03, query=True, worldSpace = True, rotation = True )
    cmds.xform(fkCtrl03,rotation = (qIkJntRot03[0],qIkJntRot03[1],qIkJntRot03[2]),worldSpace = True)




def ikToFkDef(fkCtrl01,fkCtrl02,fkCtrl03,ikCtrl,pvCtrl,ikJnt02):
    #match IK to FK, Rotate FK Joint wherever you want then run
    #fkCtrl01, fkCtrl02, fkCtrl03, ikCtrl, pvCtrl, ikJnt02
    
    qFkCtrlRot03 = cmds.xform( fkCtrl03, query=True, worldSpace = True, rotation = True )
    qFkCtrlTra03 = cmds.xform( fkCtrl03, query=True, worldSpace = True, translation = True )
    
    cmds.xform(ikCtrl,rotation = (qFkCtrlRot03[0],qFkCtrlRot03[1],qFkCtrlRot03[2]),worldSpace = True)
    cmds.xform(ikCtrl,translation = (qFkCtrlTra03[0],qFkCtrlTra03[1],qFkCtrlTra03[2]),worldSpace = True)
    
    #Create Locator and pointConstraint and aimConstraint
    
    fkPvLoc = cmds.spaceLocator( position=(0, 0, 0),name="fk_poleVectorLoc_#" )
    ptC = cmds.pointConstraint( fkCtrl01, fkCtrl02, fkCtrl03, fkPvLoc, maintainOffset=False )
    amC = cmds.aimConstraint( fkCtrl02, fkPvLoc, maintainOffset=False )
    cmds.delete(ptC)
    cmds.delete(amC)
    
    #Mesure the distance between Locator and Mid Joint
    
    mesuPosi01 = cmds.xform(fkPvLoc, query=True, relative=True, worldSpace=True, translation=True )
    mesuMidJntLoc = cmds.spaceLocator( position=(0, 0, 0),name="mesureLoc_#" )
    cmds.parentConstraint(ikJnt02, mesuMidJntLoc, maintainOffset=False)
    mesuPosi02 = cmds.xform(mesuMidJntLoc, query=True, relative=True, worldSpace=True, translation=True )
    distNode = cmds.distanceDimension( startPoint=(mesuPosi01[0], mesuPosi01[1], mesuPosi01[2]), endPoint=(mesuPosi02[0], mesuPosi02[1], mesuPosi02[2]) )
    distValue = cmds.getAttr( distNode +".distance" )
    disTrans = cmds.listRelatives(distNode,parent=True)
    
    
    cmds.delete(disTrans[0])
    cmds.delete(mesuMidJntLoc)
    
    
    #Match the Pole Vector to the Locator
    
    cmds.xform( fkPvLoc, relative=True, objectSpace=True, translation=(distValue*10, 0, 0) )
    
    prC = cmds.pointConstraint( fkPvLoc, pvCtrl, maintainOffset=False )
    cmds.delete(prC)
    cmds.delete(fkPvLoc)





def qLimbDef(lasCB,rasCB,llsCB,rlsCB,rtOM,ikfkRBG):
#    qLasCB = cmds.checkBox(lasCB, query=True, value=True)
 #   qRasCB = cmds.checkBox(rasCB, query=True, value=True)
#    qLlsCB = cmds.checkBox(llsCB, query=True, value=True)
#    qRlsCB = cmds.checkBox(rlsCB, query=True, value=True)
    qRtOM = cmds.optionMenu(rtOM, query=True, value=True)

    if cmds.checkBox(lasCB, query=True, value=True) :
        print "Run L arm switch"
        
        
        ikJnt01 = RIG_DATA[qRtOM][0]["Joints"][0]["Left Shoulder"]
        ikJnt02 = RIG_DATA[qRtOM][0]["Joints"][0]["Left Elbow"]
        ikJnt03 = RIG_DATA[qRtOM][0]["Joints"][0]["Left Wrist"]
        
        fkCtrl01 = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Shoulder"]
        fkCtrl02 = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Elbow"]
        fkCtrl03 = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Wrist"]
        
        ikCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Arm IK"]
        pvCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Elbow Pole Vector"]
        
        
        qRtOM = cmds.optionMenu(rtOM, query=True, select=True)
        qIkfkRBG = cmds.radioButtonGrp(ikfkRBG, query=True, select=True )
        if qIkfkRBG == 1:
            print "Run FK To IK"
            fkToIkDef(ikJnt01,ikJnt02,ikJnt03,fkCtrl01,fkCtrl02,fkCtrl03)            
        else:
            print "Run IK To FK"
            ikToFkDef(fkCtrl01,fkCtrl02,fkCtrl03,ikCtrl,pvCtrl,ikJnt02)
        
    if cmds.checkBox(rasCB, query=True, value=True) :
        print "Run R arm switch"

        
        ikJnt01 = RIG_DATA[qRtOM][0]["Joints"][0]["Right Shoulder"]
        ikJnt02 = RIG_DATA[qRtOM][0]["Joints"][0]["Right Elbow"]
        ikJnt03 = RIG_DATA[qRtOM][0]["Joints"][0]["Right Wrist"]
        
        fkCtrl01 = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Shoulder"]
        fkCtrl02 = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Elbow"]
        fkCtrl03 = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Wrist"]
        
        ikCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Arm IK"]
        pvCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Elbow Pole Vector"]
        
        
        
        qIkfkRBG = cmds.radioButtonGrp(ikfkRBG, query=True, select=True )
        if qIkfkRBG == 1:
            print "Run FK To IK"
            fkToIkDef(ikJnt01,ikJnt02,ikJnt03,fkCtrl01,fkCtrl02,fkCtrl03)            
        else:
            print "Run IK To FK"
            ikToFkDef(fkCtrl01,fkCtrl02,fkCtrl03,ikCtrl,pvCtrl,ikJnt02)
               
    if cmds.checkBox(llsCB, query=True, value=True) :
        print "Run L leg switch"
        
        

        
        ikJnt01 = RIG_DATA[qRtOM][0]["Joints"][0]["Left Hip"]
        ikJnt02 = RIG_DATA[qRtOM][0]["Joints"][0]["Left Knee"]
        ikJnt03 = RIG_DATA[qRtOM][0]["Joints"][0]["Left Ankle"]
        
        fkCtrl01 = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Hip"]
        fkCtrl02 = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Knee"]
        fkCtrl03 = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Ankle"]
        
        ikCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Leg IK"]
        pvCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Left Knee Pole Vector"]
        
        
        qRtOM = cmds.optionMenu(rtOM, query=True, select=True)
        qIkfkRBG = cmds.radioButtonGrp(ikfkRBG, query=True, select=True )
        if qIkfkRBG == 1:
            print "Run FK To IK"
            fkToIkDef(ikJnt01,ikJnt02,ikJnt03,fkCtrl01,fkCtrl02,fkCtrl03)            
        else:
            print "Run IK To FK"
            ikToFkDef(fkCtrl01,fkCtrl02,fkCtrl03,ikCtrl,pvCtrl,ikJnt02)
                    
    
    if cmds.checkBox(rlsCB, query=True, value=True) :
        print "Run R leg switch"

        

        
        ikJnt01 = RIG_DATA[qRtOM][0]["Joints"][0]["Right Hip"]
        ikJnt02 = RIG_DATA[qRtOM][0]["Joints"][0]["Right Knee"]
        ikJnt03 = RIG_DATA[qRtOM][0]["Joints"][0]["Right Ankle"]
        
        fkCtrl01 = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Hip"]
        fkCtrl02 = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Knee"]
        fkCtrl03 = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Ankle"]
        
        ikCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Leg IK"]
        pvCtrl = RIG_DATA[qRtOM][0]["Controlers"][0]["Right Knee Pole Vector"]
        
        
        qRtOM = cmds.optionMenu(rtOM, query=True, select=True)
        qIkfkRBG = cmds.radioButtonGrp(ikfkRBG, query=True, select=True )
        if qIkfkRBG == 1:
            print "Run FK To IK"
            fkToIkDef(ikJnt01,ikJnt02,ikJnt03,fkCtrl01,fkCtrl02,fkCtrl03)            
        else:
            print "Run IK To FK"
            ikToFkDef(fkCtrl01,fkCtrl02,fkCtrl03,ikCtrl,pvCtrl,ikJnt02)
                    




def fkIkSUI(): 

    getCharData()

    fkIkSWin = "fkIkSwitchWin"
    if cmds.window(fkIkSWin, exists=True):
        cmds.deleteUI(fkIkSWin)
    if cmds.windowPref(fkIkSWin, exists=True):
        cmds.windowPref(fkIkSWin, remove=True)
    
    winWidth = 300
    winHeight = 270
    
    cmds.window(fkIkSWin, width=winWidth, height=winHeight, menuBar=True, sizeable=True, title="FK IK Switch")
    
    cmds.menu(label="Help")
    cmds.menuItem(label="About...", command="glr_aboutWin()")
    
    cmds.frameLayout(borderVisible=True, borderStyle="etchedIn", labelVisible=False)
    mainForm = cmds.formLayout("mainForm")
    
    rtTxt = cmds.text("rtTxt", label="Rig Type :", font="boldLabelFont")
    cmds.formLayout(mainForm, edit=True, attachForm=[(rtTxt, "left", 43), (rtTxt, "top", 20)])
    
    rtOM = cmds.optionMenu("rtOM")
    cmds.menuItem(label="biped")
    cmds.menuItem(label="quadruped")
    cmds.formLayout(mainForm, edit=True, attachControl=[rtOM, "left", 5, rtTxt], attachForm=[(rtOM, "left", 125),(rtOM, "top", 18)])
    qRtOM = cmds.optionMenu(rtOM, query=True, value=True)
    lasCB = cmds.checkBox("lasCB", label=RIG_DATA[qRtOM][0]["Check Boxes"][0])
    cmds.formLayout(mainForm, edit=True, attachControl=[lasCB, "top", 15, rtOM], attachForm=[(lasCB, "left", 103)])
    rasCB = cmds.checkBox("rasCB", label=RIG_DATA[qRtOM][0]["Check Boxes"][1])
    cmds.formLayout(mainForm, edit=True, attachControl=[rasCB, "top", 15, lasCB], attachForm=[(rasCB, "left", 103)])
    llsCB = cmds.checkBox("llsCB", label=RIG_DATA[qRtOM][0]["Check Boxes"][2])
    cmds.formLayout(mainForm, edit=True, attachControl=[llsCB, "top", 15, rasCB], attachForm=[(llsCB, "left", 103)])
    rlsCB = cmds.checkBox("rlsCB", label=RIG_DATA[qRtOM][0]["Check Boxes"][3])
    cmds.formLayout(mainForm, edit=True, attachControl=[rlsCB, "top", 15, llsCB], attachForm=[(rlsCB, "left", 103)])
    
        
    sep = cmds.separator("sep", style="in")
    smTxt = cmds.text("smTxt", label="Select Mode :", font="boldLabelFont")
    cmds.formLayout(mainForm, edit=True, attachForm=[(smTxt, "left", 20), (smTxt, "bottom", 40)])
    
    
    ikfkRBG = cmds.radioButtonGrp( label=" ", labelArray2=["FK To IK", "IK To FK"], numberOfRadioButtons=2,select=1)
    cmds.formLayout(mainForm, edit=True, attachForm=[(ikfkRBG, "bottom", 35), (ikfkRBG, "left", -40)])
    
    sep2 = cmds.separator("sep2", style="in")
    createBtn = cmds.button("createBtn", label="OK", command=("print ('Success!');from ikfkSwitch import ikfkSwitch; ikfkSwitch.qLimbDef('" + lasCB + "','" + rasCB + "','" + llsCB + "','" + rlsCB + "','" + rtOM + "','" + ikfkRBG + "')"))
    cancelBtn = cmds.button("cancelBtn", label="Cancel", command=("from maya import cmds;cmds.deleteUI('" + fkIkSWin + "')"))
    
    cmds.formLayout(mainForm, edit=True, attachForm=[(sep2, "left", 0), (sep2, "right", 0), (sep2, "bottom", 60)])    
    cmds.formLayout(mainForm, edit=True, attachForm=[(sep, "left", 0), (sep, "right", 0), (sep, "bottom", 25)])
    cmds.formLayout(mainForm, edit=True, attachForm=[(createBtn, "left", 0), (createBtn, "bottom", 0)], attachControl=[(createBtn, "top", 0, sep)], attachPosition=[(createBtn, "right", 0, 50)])
    cmds.formLayout(mainForm, edit=True, attachControl=[(cancelBtn, "left", 0, createBtn), (cancelBtn, "top", 0, sep)], attachForm=[(cancelBtn, "right", 0), (cancelBtn, "bottom", 0)])
    
    
    #Place code here for UI guts
    
    
    
    cmds.window(fkIkSWin, edit=True, width=winWidth, height=winHeight)
    
    cmds.showWindow(fkIkSWin)










