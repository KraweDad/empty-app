from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
xcoordinates = range(100, 600, 10)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x, x*0.5 + 100)) for x in xcoordinates]

myapp = App()
myapp.run()
