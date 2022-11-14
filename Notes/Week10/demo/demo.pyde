xpos = 0
red_channel = 0

def setup():
    """Setup runs this code once when you first launch your sketch."""
    size(500, 300)

def draw():
    """runs repeatedly over and over again,
    approximately sixty times per second,
    codes should be brief instead of time-consuming
    """
    global xpos
    global red_channel
    background(100, 150, 150)

    # decide filling color
    fill(red_channel/2, 100,100)

    # decide the weight of stroke
    strokeWeight(5)

    # decide color of stroke
    stroke(255)

    # fill the ellipse with the filling color, stroke color
    ellipse(xpos,150,50,50)

    fill(255, 255, 0)
    noStroke()
    ellipse(mouseX, mouseY, 20, 20)

    xpos+=1
    red_channel +=1
