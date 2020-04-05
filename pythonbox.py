from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
from direct.actor.Actor import Actor
from panda3d.core import *

 
class MyApp(ShowBase):
 
  def __init__(self):
    ShowBase.__init__(self)

    # Load the environment model.
    self.box = Actor("Box2.egg")
    
    
    # Reparent the model to render.
    self.box.reparentTo(self.render)
    # Apply scale and position transforms on the model.
    self.box.setScale(0.5, 0.5, 0.5)
    
    self.box.setPos(0, 5, -1)

    red = Material()
    self.box.setMaterial(red,1)


    # set light
    ambientLight = AmbientLight("ambientLight")
    ambientLight.setColor((.8, .8, .75, 1))
    directionalLight = DirectionalLight("directionalLight")
    directionalLight.setDirection(LVector3(0, 0, -2.5))
    directionalLight.setColor((0.9, 0.8, 0.9, 1))
    render.setLight(render.attachNewNode(ambientLight))
    render.setLight(render.attachNewNode(directionalLight))

 
class ReadKeys(DirectObject.DirectObject):
  def __init__(self, model):
    
    print("ReadKeys constructor")
    self.accept('a', self.openBox)
    self.accept('b', self.closeBox)

    self.model = model
    print("use \"a\" key to open box")
    print("use \"b\" key to close box")
 
  def openBox(self):
    self.model.play('openBox')
    
  def closeBox(self):
    self.model.play('closeBox')
    

m = MyApp()
r = ReadKeys(m.box)
m.run()
