from itertools import permutations

def area(l, h, w):
    return(l*h*w)

def surf_area(l, h, w):
    return(((l*h)+(l*w)+(w*h))*2)

for length, height, width in permutations(range(1,100),3):
    if area(length, height, width)== surf_area(length, height, width):
        print("length = {}, height = {}, width = {}".format(length,height,width))
