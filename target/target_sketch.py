"""
pyp5js
Copyright (C) 2019-2021 Bernardo Fontes

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from pyp5js import *

def preload():
    pass

def setup():
    pass

def draw():
    pass

deviceMoved = None
deviceTurned = None
deviceShaken = None
keyPressed = None
keyReleased = None
keyTyped = None
mouseMoved = None
mouseDragged = None
mousePressed = None
mouseReleased = None
mouseClicked = None
doubleClicked = None
mouseWheel = None
touchStarted = None
touchMoved = None
touchEnded = None
windowResized = None
keyIsDown = None


gmagnitude = 0.003

class eye():
    def __init__(self, x, y, magnitude):
        self.x = x
        self.originX = x
        self.y = y
        self.originY = y
        self.originMagnitude = magnitude 
        self.magnitude = magnitude
        self.distX = 0
        self.distY = 0
        self.radiusX = 12
        self.radiusY = 5
        
    def update(self):
        self.distX = mouseX-self.x
        self.distY = mouseY-self.y
                
        if (abs(self.x-self.originX)) <= self.radiusX:
            self.magnitude = self.originMagnitude
            self.x = self.x + (self.distX * self.magnitude)
        else:
            print(abs(((self.x-self.originX))-self.radiusX))
            if self.x > self.originX:
                self.x = self.x - (abs(((self.x-self.originX))-self.radiusX))
            else:
                self.x = self.x + (abs(((self.x-self.originX))+self.radiusX))

            #self.x = self.x (
            self.magnitude = 0
        if (abs(self.y-self.originY)) <= self.radiusY:
            self.magnitude = self.originMagnitude
            self.y = self.y + (self.distY * self.magnitude)
        else:
            if self.y > self.originY:
                self.y = self.y - (abs(((self.y-self.originY))-self.radiusY))
            else:
                self.y = self.y + (abs(((self.y-self.originY))+self.radiusY))



    def display(self):
        fill(0)
        ellipse(self.x, self.y, 15, 15)
        
img = []

def setup():
    size(503, 589)
    global img
    img = loadImage("logofunctional.png")
    noStroke()
    
eyel = eye(185, 250, gmagnitude)
eyer = eye(313, 250, gmagnitude)

def draw():
    background(0)
    fill(0)
    rect(0, 0, 502, 588)
    fill(255)
    rect(150, 235, 200, 50)
    eyel.update()
    eyer.update()
    eyel.display()
    eyer.display()
    fill(0)
    image(img, 2, 2)
    


event_functions = {
    "deviceMoved": deviceMoved,
    "deviceTurned": deviceTurned,
    "deviceShaken": deviceShaken,
    "keyPressed": keyPressed,
    "keyReleased": keyReleased,
    "keyTyped": keyTyped,
    "mouseMoved": mouseMoved,
    "mouseDragged": mouseDragged,
    "mousePressed": mousePressed,
    "mouseReleased": mouseReleased,
    "mouseClicked": mouseClicked,
    "doubleClicked": doubleClicked,
    "mouseWheel": mouseWheel,
    "touchStarted": touchStarted,
    "touchMoved": touchMoved,
    "touchEnded": touchEnded,
    "windowResized": windowResized,
    "keyIsDown": keyIsDown,
}

start_p5(preload, setup, draw, event_functions)