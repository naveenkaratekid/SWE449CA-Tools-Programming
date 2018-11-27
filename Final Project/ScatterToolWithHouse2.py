import maya.cmds as mc
import random
import OptionsWindowBaseClass

class ScatterHouse(OptionsWindowBaseClass.OptionsWindow):
    """Custom Window Class, subclass of the OptionWindow base class """
   
        
    def __init__(self):
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title = "ScatterHouse"
        self.actionName = "Scatter House"
        self.applyName = "Add Ground"
    
    def displayOptions(self):
        
        self.objType = mc.radioButtonGrp(label = "Object Type:", label1 = "House", numberOfRadioButtons = 1, select=1)
       
        self.xformGrp = mc.frameLayout(label = "Mesh Object Generator", collapsable = True)
        mc.formLayout(self.optionsForm, e = True, attachControl=([self.xformGrp, "top",2,self.objType]), attachForm = ([self.xformGrp, "left",0],[self.xformGrp,"right",0]))
        
        self.xformCol = mc.columnLayout()
        self.position = mc.floatFieldGrp(label = "Range of Translation:",numberOfFields=3, value = [10.0,10.0,10.0,10.0])
        self.rotation = mc.floatFieldGrp(label = "Range of Rotations:",numberOfFields=3, value = [180.0,180.0,180.0,180.0])
        self.scale = mc.floatFieldGrp(label =  "Range of Scale:",numberOfFields=3,value = [3.0,3.0,3.0,3.0])
        self.num = mc.intFieldGrp( label = "Number of Houses", numberOfFields = 1, value1 = 5)
        mc.setParent(self.optionsForm)
        
        
           
    def actionCmd(self,*args):
        """ actionCmd() will be called when the user presses the Scatter House button 
        This function will read values set by the user and create and possition
        the houses"""
   
        self.objIndAsCmd= { 1 : mc.polyCube, 2 : mc.polyCone, 3 : mc.polyCylinder, 4 : mc.polySphere}
        
      
        self.rangeX = mc.floatFieldGrp(self.position, query = True, value1 = True)
        self.rangeY = mc.floatFieldGrp(self.position, query = True, value2 = True)
        self.rangeZ = mc.floatFieldGrp(self.position, query = True, value3 = True)
        
        self.rotX = mc.floatFieldGrp(self.rotation, query = True, value1 = True)
        self.rotY = mc.floatFieldGrp(self.rotation, query = True, value2 = True)
        self.rotZ = mc.floatFieldGrp(self.rotation, query = True, value3 = True)
        
        self.scaleX = mc.floatFieldGrp(self.scale, query = True, value1 = True)
        self.scaleY = mc.floatFieldGrp(self.scale, query = True, value2 = True)
        self.scaleZ = mc.floatFieldGrp(self.scale, query = True, value3 = True)
        
       	self.numberOfObjects = mc.intFieldGrp(self.num, q = True, value1 = True)
       
        createHouse(self.scaleX, self.scaleY, self.scaleZ, random.uniform(0.0,1.0), random.uniform(0.0,1.0), random.uniform(0.0,1.0), self.numberOfObjects, self.rangeX, self.rangeY, self.rangeZ,self.rotX,self.rotY,self.rotZ )
        """
        applyBtnCmd() function will be called when user presses
        AddGround button. It will create a ground object, turn it into
        passive rigid object in Maya, and loop over all other polygonal objects
        and turn them into active rigid objects. It will connect all active RB to
        gravity
        """
    def applyBtnCmd(self,*args):        
       	ground1 = mc.polyPlane()
        #move the ground plane under the lowest possible object
        for i in range(self.numberOfObjects):
        	mc.setAttr(ground1[0] + ".translateY", -self.rangeX)
        	mc.setAttr(ground1[0] + ".translateX", 0)
        	mc.setAttr(ground1[0] + ".translateZ", 98)
        	mc.setAttr(ground1[0] + ".scaleX", 120)
        	mc.setAttr(ground1[0] + ".scaleY", 1)
        	mc.setAttr(ground1[0] + ".scaleZ", self.rangeZ * (i + 1) * self.numberOfObjects - 10)
        	currentX = mc.getAttr('house.translateX')
        	print currentX
      	  	if self.numberOfObjects < 5:
        		mc.setAttr(ground1[0] + ".scaleZ", 208)
        		mc.setAttr(ground1[0] + ".translateZ", 2.7)
        		

    
"""
	createHouse(scaleX, scaley, scaleZ, r,g,b) will 
	draw a specific kind of house with predefined specs as seen throughout this function. The components of the house will be combined
	into a single object, and then that entire object will be resized by a random generator. 

	This procedure will return the house object

"""

def createHouse(scaleX, scaleY, scaleZ, r,g,b, numOfHouses, randX, randY, randZ, rotateX, rotateY, rotateZ):
				
		for i in range(numOfHouses):
			
			# Create new scene every time program runs
			mc.file(new = True, force = True) 
			"""
	        Below, we create the roof for the house
	        """
	                # Roof
	                roof = mc.polyPyramid(n='roof')
	                mc.scale(28.147,12.410,28.373)
	                mc.move(1.167, 32.273, 0)
	                mc.setAttr('roof.ry', 45)
	                colorLambert = mc.shadingNode('lambert', asShader=True) 
	                mc.select(roof)
	                
	                # ColorLambert and HyperShade are for setting color of the object
	                
	                mc.setAttr((colorLambert + '.color'), r, g, b, type = 'double3')

	                mc.hyperShade(assign=colorLambert)
	                mc.polyMoveVertex('roof.vtx[0:1]', tx=-25.3)
	                mc.polyMoveVertex('roof.vtx[4]', tx=-10.3)
	                
	                # Roof 2
	                roof2 = mc.polyPyramid(n='roof2')
	                mc.scale(28.147,12.410,28.373)
	                mc.move(1.167, 28.601, -28.944)
	                mc.setAttr('roof2.rx', -20.000)
	                mc.setAttr('roof2.ry', 43.000)
	                mc.setAttr('roof2.rz', -13.500)
	                colorLambert = mc.shadingNode('lambert', asShader=True) 
	                mc.select(roof2)
	                #mc.setAttr((colorLambert + '.color'), 0.5725, 0.1686, 0.129, type = 'double3')
	               	mc.setAttr((colorLambert + '.color'), r, g, b, type = 'double3')

	                mc.hyperShade(assign=colorLambert)
	                mc.polyMoveVertex('roof2.vtx[0:1]', tx=-25.3)
	                mc.polyMoveVertex('roof2.vtx[4]', tx=-10.3)
	                
	                """
	                Below, we create the windows for the house
	                """
	                # Windows
	                
	                # Front top above garage
	                for i in range(1):
	                        windows = mc.polyCube(n='windowsFrontTop')
	                        mc.scale(0.420, 5.886, 9.002)
	                        mc.move(11.975, 23.622, -10.279 * -i)
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(windows)
	                        mc.setAttr((colorLambert + '.color'), 0, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                
	                # Left Side on 2nd story
	                for i in range(0,2):
	                        windows = mc.polyCube(n='windowsRightSideBottom')
	                        mc.scale(0.420, 3.325, 5.290)
	                        mc.rotate(0,90,0)
	                        mc.move(-15.612 * i, 23.622, 13.253)
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(windows)
	                        mc.setAttr((colorLambert + '.color'), 0, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                
	                # Rear windows on 2nd story
	                for i in range(-1,1):
	                        windows = mc.polyCube(n='windowsFrontBottom')
	                        mc.scale(0.420, 3, 2.940)
	                        mc.move(-33.978, 23.622, 8.921 * -i)
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(windows)
	                        mc.setAttr((colorLambert + '.color'), 0, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                        
	                # 2 end windows near Front Door
	                for i in range(2):
	                        frontDoorEndWindow = mc.polyCube(n='frontDoorEndWindow')
	                        mc.scale(0.627, 4.665, 2.428)
	                        mc.move(-4.546, 13.984, -27.740 - (10*i))
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(frontDoorEndWindow)
	                        mc.setAttr((colorLambert + '.color'), 0, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                
	                # Window near Front Door
	                for i in range(1):
	                        frontDoorWindow = mc.polyCube(n='frontDoorWindow')
	                        mc.scale(0.627, 4.665, 7.094)
	                        mc.move(-4.546, 13.984, -32.742)
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(frontDoorWindow)
	                        #mc.setAttr((colorLambert + '.color'), 0.412, 0.412, 0.412, type = 'double3' )
	                        mc.setAttr((colorLambert + '.color'), random.uniform(0.0,1.0), random.uniform(0.0,1.0), random.uniform(0.0,1.0), type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                        
	                                
	                # Rear window near ground floor bedroom
	                for i in range(1):
	                        windowsRearBottomNearBedroom = mc.polyCube(n='windowsRearBottomNearBedroom')
	                        mc.scale(0.420, 3, 6.388)
	                        mc.move(-33.978, 14.686, -19.139)
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(windowsRearBottomNearBedroom)
	                        mc.setAttr((colorLambert + '.color'), 0, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                
	                # Rear window near kitchen
	                for i in range(1):
	                        windowsRearBottomNearKitchen = mc.polyCube(n='windowsRearBottomNearKitchen')
	                        mc.scale(0.420, 7.818, 4.556)
	                        mc.move(-33.978, 10.546, -36.449)
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(windowsRearBottomNearKitchen)
	                        mc.setAttr((colorLambert + '.color'), 0, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	        
	                """
	                Below, we create the main and right side of the building for the house
	                """
	                # main building
	                building = mc.polyCube(n='building')
	                mc.scale(25.963, 26.190, 45.551)
	                mc.move(-10.958, 14.810, 0)
	                mc.setAttr('building.ry', 90)
	                colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                mc.select(building)
	                #mc.setAttr((colorLambert + '.color'), r, g, b, type = 'double3' )
	                mc.setAttr((colorLambert + '.color'), random.uniform(0.0,1.0), random.uniform(0.0,1.0), random.uniform(0.0,1.0), type = 'double3' )
	                mc.hyperShade(assign=colorLambert)
	                mc.polySplitVertex('building.vtx[2:5]')
	                
	                # Right side of building
	                rightSide = mc.polyCube(n='rightSide')
	                mc.scale(28.082, 7.793, 29.276)
	                mc.rotate(0,90,0)
	                mc.move(-19.041, 5.623, -26.999)
	                colorLambert = mc.shadingNode('lambert', asShader=True) 
	                mc.select(rightSide)
	                #mc.setAttr((colorLambert + '.color'), r, g, b, type = 'double3' )
	                mc.setAttr((colorLambert + '.color'), random.uniform(0.0,1.0), random.uniform(0.0,1.0), random.uniform(0.0,1.0), type = 'double3' )
	                mc.hyperShade(assign=colorLambert)
	                mc.polyMoveVertex('rightSide.vtx[2]', 'rightSide.vtx[4]', ty=18.4)
	                mc.polyMoveVertex('rightSide.vtx[3]', 'rightSide.vtx[5]', ty=10)
	                mc.polyMoveVertex('rightSide.vtx[3]', ty=1)
	                mc.polyMoveVertex('rightSide.vtx[5]', ty=1)
	                
	                """
	                Below, we create the front doors and the garage door
	                """
	                # 2 Front Doors
	                for i in range(2):
	                        frontDoor = mc.polyCube(n='frontDoor')
	                        mc.scale(0.627, 8.678, 4.392)
	                        mc.move(-4.546, 6.086, -15.466 - (4.5*i))
	                        colorLambert = mc.shadingNode( 'lambert', asShader=True ) 
	                        mc.select(frontDoor)
	                        mc.setAttr((colorLambert + '.color'), 0.5, 0, 0, type = 'double3' )
	                        mc.hyperShade(assign=colorLambert)
	                
	                # Garage Door
	                for i in range(1):	
	                        garageDoor = mc.polyCube(n='garageDoor')
	                        mc.move(11.982,6.060 + (2.35*i),0)
	                        mc.scale(0.277, 8.664, 18.652)
	                        mc.select(garageDoor)
	                        
	                
	                # polyUnite() will gather the objects and will merge all of them together. This allows to scale the entire house without having to worry about modifying the coordinates of the windows, roof, and other components of the house
	                house = mc.polyUnite('rightSide', 'building','garageDoor', 'windowsRightSideBottom', 'windowsRightSideBottom1', 'windowsFrontBottom1', 'windowsFrontTop', 'frontDoorEndWindow1', 'roof', 'frontDoor1', 'frontDoor', 'roof2','windowsFrontBottom','windowsRearBottomNearKitchen','windowsRearBottomNearBedroom','frontDoorWindow','frontDoorEndWindow', n='house')
	                mc.setAttr('house.translateX', 54)     
	                
	                # Here we are spawning the number of houses into the scene
	                for i in range(1,numOfHouses):
	                	mc.scale(scaleX / 10, scaleY / 10, scaleZ / 10, house)
	                 	mc.duplicate('house', smartTransform=False)
	                 	mc.setAttr('house.translateX', 54)
	                	mc.setAttr('house%d.rx' % i, rotateX)
	                	mc.setAttr('house%d.ry' % i, rotateY)
	                	mc.setAttr('house%d.rz' % i, rotateZ)
	                	
	                	mc.setAttr('house%d.tx' % i, 54 - randX)
	                	mc.setAttr('house%d.ty' % i, 2 * i * randY)
	                	mc.setAttr('house%d.tz' % i, i * 5 * randZ)

	                	#mc.xform('house%d' % i, translation=[54 - randX, 2 * i * randY, 5 * i * randZ])

	                return house # Now we return the object	

win = ScatterHouse()
win.create()
