"imports"
import random
import matplotlib.pyplot as plt 

def calling_steps():

    while True:

        try:
            steps = int(input('number of steps: '))
        except ValueError:
            print("invalid input")

        if steps > 0:
            return steps 
        else:
            print('more than 0 moron ')

def rand_walk(steps):

    x, y = 0, 0
    v = (x,y)
    position_list.append(v)


    for i in range(steps):

        xo, yo = x, y

        e = random.randint(-100, 100) # random value for distance for each iteration
        i = random.randint(-100, 100) # random value for distance for each iteration
        val = random.randint(1, 8) # random value deciding which direction 

        if val == 1:
            x = xo + e
            y = yo
        elif val == 2:
            x = xo - e
            y = yo
        elif val == 3:
            x = xo + e
            y = yo - i
        elif val == 4:
            x = xo - e
            y = yo - i
        elif val == 5:
            x = xo + e
            y = yo + i
        elif val == 6:
            x = xo - e
            y = yo + i
        elif val == 7:
            x = xo
            y = yo + i
        else:
            x = xo
            y = yo - i
        
        v = (x, y)
        position_list.append(v) #current position is appended to list

def plotting_data(position_list):

    xs = [x[0] for x in position_list] # create a list of each position in the x direction
    ys = [x[1] for x in position_list]

    fig1 = plt.figure(1)
    plt.plot(xs, ys)
    plt.show()


position_list = []

steps = calling_steps()

rand_walk(steps)

plotting_data(position_list)















    