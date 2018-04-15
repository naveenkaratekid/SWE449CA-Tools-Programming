import maya.cmds as mc
from random import *
import os
import OptionsWindowBaseClass
#import houseWindow
"""
makeHouse()

Naveen K

3-31-18

SWE449 Tools Programming

"""

#mc.file(new = True, force = True)

class MakeHouse(OptionsWindowBaseClass.OptionsWindow):
	def __init__(self):
		OptionsWindowBaseClass.OptionsWindow.__init__(self)
		self.title = "House Generator"
		self.actionName = "Construct House"
		self.applyName = "Apply" 
	
	def displayOptions(self):
                mc.columnLayout("mainColumnLayout", rs=10)
                mc.text(label="Enter the name of house: ")
                self.houseName = mc.textField("houseNameField", text="", w=500)
                mc.text(label="Scale X: ")
                self.x = mc.floatField("scaleX", w=100)
                mc.text(label="Scale Y: ")
                self.y = mc.floatField("scaleY", w=100)
                mc.text(label="Scale Z: ")
                self.z = mc.floatField("scaleZ", w=100)
                mc.rowColumnLayout(rs=[1,1])
                mc.setParent("..")
                mc.columnLayout(rs=20)
                
                self.r = mc.floatSliderGrp("R",l="Red: ", cw3=[100,50,200],cal=[(1,"center"),(2,"center"),(3,"center")],f=True, pre=3, min=0.00,max=1.00,v=0.00)
                self.g = mc.floatSliderGrp("G",l="Green: ", cw3=[100,50,200],cal=[(1,"center"),(2,"center"),(3,"center")],f=True,pre=3, min=0.00,max=1.00,v=0.00)
                self.b = mc.floatSliderGrp("B",l="Blue: ", cw3=[100,50,200],cal=[(1,"center"),(2,"center"),(3,"center")],f=True, pre=3,min=0.00,max=1.00,v=0.00)
                
                mc.rowColumnLayout(rs=[10,10])
                mc.text(label="Number of Houses: ")
                self.numOfHouses = mc.intField("Num of houses", w=100)

	
	"""
		createHouse(scaleX, scaley, scaleZ, r,g,b) will 
		draw a specific kind of house with predefined specs as seen throughout this function. The components of the house will be combined
		into a single object, and then that entire object will be resized by a random generator. 
	
		This procedure will return the house object
	
	"""
	
	def actionCmd(self, *args):
	    
	   self.name = mc.textField(self.houseName, query = True, text = True)
	   self.scalex = mc.floatField(self.x, query = True, value = True)
	   self.scaley = mc.floatField(self.y, query = True, value = True)
	   self.scalez = mc.floatField(self.z, query = True, value = True)
	   self.red = mc.floatSliderGrp(self.r, query = True, value = True)
	   self.green = mc.floatSliderGrp(self.g, query = True, value = True)
	   self.blue = mc.floatSliderGrp(self.b, query = True, value = True)
	   self.houseAmnt = mc.intField(self.numOfHouses, q=True, v=True)
	   
	   self.createHouse(self.scalex, self.scaley, self.scalez, self.red, self.green, self.blue, self.houseAmnt)
	
	def createHouse(self,scaleX, scaleY, scaleZ, r,g,b, numOfHouses):
		
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
                mc.setAttr((colorLambert + '.color'), 0.5725, 0.1686, 0.129, type = 'double3')
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
                mc.setAttr((colorLambert + '.color'), 0.5725, 0.1686, 0.129, type = 'double3')
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
                        mc.setAttr((colorLambert + '.color'), 0.412, 0.412, 0.412, type = 'double3' )
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
                mc.setAttr((colorLambert + '.color'), r, g, b, type = 'double3' )
                mc.hyperShade(assign=colorLambert)
                mc.polySplitVertex('building.vtx[2:5]')
                
                # Right side of building
                rightSide = mc.polyCube(n='rightSide')
                mc.scale(28.082, 7.793, 29.276)
                mc.rotate(0,90,0)
                mc.move(-19.041, 5.623, -26.999)
                colorLambert = mc.shadingNode('lambert', asShader=True) 
                mc.select(rightSide)
                mc.setAttr((colorLambert + '.color'), r, g, b, type = 'double3' )
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
                
                # Scale the house from the random x,y,z sizes
                mc.scale(scaleX,scaleY,scaleZ, house)
                
                """for i in range(numOfHouses):
                	mc.duplicate('house', smartTransform=True)
                	mc.xform(house, translation=[i * 10, i, i * 5])"""
                return house # Now we return the object

	
	
	# Saving the maya scene into the directory
	home = os.getenv("HOME") + "/maya/projects/default/scenes" # Note: This saves the maya scene in the scenes directory. Located under maya/projects/default/
	mc.file(rename = os.path.join(home,"procMayaScene_nkmurthy.mb"))
	mc.file(save = True)


win = MakeHouse()
win.create()
