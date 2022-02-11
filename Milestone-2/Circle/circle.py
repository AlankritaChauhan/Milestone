import turtle

c=turtle.Turtle()
c.pen(pencolor="purple",fillcolor="orange")
r=50
for i in range(4):
    c.circle(r)
    r=r-10


turtle.done()
