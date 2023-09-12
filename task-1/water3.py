def initial_state():
    return (0, 0, 0)

def is_goal(s):
    return True

def successors(s):
    x, y, z = s
    if (y<5 and x>=5): yield ((x-(5-y),5,z),5)
    if (y+z<=5 and z!=0): yield((x,y+z,0),z)
    if (y+z>5 and z!=0): yield((x,5,x-(5-y)),5-y)
    if (z<3 and x>=3): yield((x-(3-z),y,3),3)
    if (y+z<=3 and y!=0): yield((x,0,y+z),y)
    if (y+z>3 and y!=0): yield((x,y-(3-z),3),3-z)
    if (y!=0): yield((x+y,0,z),y)
    if (z!=0): yield((x+z,y,0),z)



