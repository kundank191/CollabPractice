"""
This program deals with the calculation related to bernoulli's theorem in fm lab
"""
#here are the default values of height of water collected and time
height = 8.5 #unit is cm
time = 30 #unit is seconds

#print all the hp values which is the height level of the water in cm in each perizometer , this is 
#equivalent to p/p*g , and also their distances
def getHpAndDistanceOfPiezometer():
    heights = [32,31.2,29.1,25.8,20.9,32.5,24,24.5,25.5]
    distances = [3,6,9,12,15,18,21,24,27,30,33,36]
    print("Peizometeric heights : ",heights[0:])
    print("Peizometers distances : ",distances[0:])

#returns the rate of dischage , when height of water in the container and the time required is given
def getQ(heightOfWaterCollected,time):
    #unit of area is cm2 , this is area of the container
    area = 1000
    #unit of Q is cm3/s
    Q = heightOfWaterCollected * area / time
    return Q

#prints all the velocity at all the outlets
def getVelocity(Q):
    #This variable stores all the areas of all the outlets int cm2
    area = [6.1575,4.7143,3.463,2.405,1.539,2.405,3.463,4.7143,6.1575]
    i = 1
    velocities = []
    velocityHead = []
    for a in area:
        velocity = Q/a
        velocities.append(format(velocity,'.2f'))
        velocityHead.append(format((velocity * velocity / (2 * 980)),'.2f'))
        i += 1
    print("Velocities v :", velocities[0:])
    print("Velocity head v2/2*g :", velocityHead)

Q = getQ(height,time)
getVelocity(Q)
getHpAndDistanceOfPiezometer()