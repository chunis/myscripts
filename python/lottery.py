#!/usr/bin/python

# double-color balls lottery guesser: produce 6 red balls, and 1 blue ball
# Don't complain me if it always guess wrong  :)


import random

def get_ball(start, end, picked):
    balls = set(range(start, end+1))
    balls -= picked
    picked.add(random.choice(list(balls)))

def get_red_balls():
    red = set()
    get_ball(1, 11, red)
    get_ball(1, 11, red)
    get_ball(12, 22, red)
    get_ball(12, 22, red)
    get_ball(23, 33, red)
    get_ball(23, 33, red)
    return sorted(list(red))

def get_blue_balls(start=1, end=15):
    return random.randint(start, end)

if __name__ == '__main__':
    print "A: red = %s, blue = %d" %(get_red_balls(), get_blue_balls(1, 5))
    print "B: red = %s, blue = %d" %(get_red_balls(), get_blue_balls(6, 10))
    print "C: red = %s, blue = %d" %(get_red_balls(), get_blue_balls(11, 15))
