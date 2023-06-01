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
        
def setup():
    url = "https://lh5.googleusercontent.com/lwD8-1x3CmpZKnEm8J9ntI4WSJtTauyMAuMJ4ZUnqwus_ue4rjOOjHP5VBKygMVBdogmGXW1p7TmYFmQ3A4ymNU"
    
    size(500, 586)
    global webImg
    webImg = loadImage(url, "png")
    noStroke()
    
eyel = eye(185, 250, gmagnitude)
eyer = eye(313, 250, gmagnitude)

def draw():
    background(255)
    rect(0, 0, 500, 586)
    fill(0)
    eyel.update()
    eyer.update()
    eyel.display()
    eyer.display()
    fill(255)
    image(webImg, 0, 0)
    