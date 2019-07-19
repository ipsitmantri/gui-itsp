from implibs import *

def make_quads(points): #this function makes all possible quads from list of centers of stars namly points
    all_quads = it.combinations(points,4)
    all_quads = [list(element) for element in all_quads]
    return list(all_quads)#returns list of all quads

def distance(point1,point2):#this function finds the distance between two points
    x1,y1 = point1
    x2,y2 = point2
    dx = x1-x2
    dy = y1-y2
    return math.sqrt(dx**2+dy**2)

def mid_point(point1,point2):#this function finds the mid point of two poiints
    x1,y1 = point1
    x2,y2 = point2
    return ((x1+x2)/2,(y1+y2)/2)#returns a point

def make_hashcodes(points): #the points represent the coordinates of 4 vertices
    combs = it.combinations(points,2) #we make combinations of 2 from the 4 stars
    combs = list(combs)
    max_dist = -1
    for i in combs: #we find the maximum of the 6 distances
        if distance(i[0],i[1]) > max_dist:
            max_dist = distance(i[0],i[1])
            A = i[0]
            B = i[1]
        else:
            pass

    for i in range(len(points)):#we delete the two fartest points in hash code as they are same in all i.e, they correspond to (0,0) &(1,1) after rotation
        if points[i] == A:
            del points[i]
            break
    for j in range(len(points)):
        if points[j] == B:
            del points[j]
            break
    C,D = points

    B1 = B.copy()
    C1 = C.copy()
    D1 = D.copy()

 #the pixel coordinate system has origin at left top corner, and rows corresponds to y axis and columns to x axis. we convert it to normal coordinate system.
    A[0],A[1] = A[1],-A[0]
    B1[0],B1[1] = B[1],-B[0]
    C1[0],C1[1] = C[1],-C[0]
    D1[0],D1[1] = D[1],-D[0]

  #we change the origin wrt to point A( hence, A becomes (0,0) )
    for i in range(2):
        B1[i] = B1[i] - A[i]
        C1[i] = C1[i] - A[i]
        D1[i] = D1[i] - A[i]

    A=np.array([[0],[0]])

 #resizing it to fit the quad in a unit circle, now the distance between A and B is root2.
    ratio = math.sqrt(2)/max_dist
    for i in range(2):
        B1[i] = B1[i] * ratio
        C1[i] = C1[i] * ratio
        D1[i] = D1[i] * ratio

#we find the angle that line AB makes
    if B1[0]==0:
        if B1[1]>0:
            theta1=np.pi/2
        else:
            theta1=1.5*np.pi
    else:
        theta1 = np.arctan(B1[1]/B1[0])
        if B1[0] > 0:
            theta1 = theta1
        elif B1[0] < 0:
            theta1 = theta1 - np.pi
        else:
            pass

  #we find the angle by which we should rotate to make it 45deg
    theta = np.pi/4 - theta1

 #we create the rotation matrix that changes the coordinates as per our required
    rot_matrix = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    B1 = np.array([[B1[0]],[B1[1]]])
    C1 = np.array([[C1[0]],[C1[1]]])
    D1 = np.array([[D1[0]],[D1[1]]])
    B1 = np.dot(rot_matrix,B1)
    C1 = np.dot(rot_matrix,C1)
    D1 = np.dot(rot_matrix,D1)


   #in our hash code C should be less than D, and both intern be less than 0.5
    if D1[0] + C1[0] >= 1:
        if D1[0] > 0.5 :
            D1[0] = 1-D1[0]
            D1[1] = 1- D1[1]
        else:
            pass
        if C1[0] > 0.5 :
            C1[0] = 1-C1[0]
            C1[1] = 1- C1[1]
        else:
            pass
    else:
        pass


    if D1[0] <= C1[0] and C1[0] + D1[0] <=1 :
        temp = D1
        D1 = C1
        C1 = temp
    elif C1[0] <= D1[0] and C1[0] + D1[0] <=1 :
        C1 = C1
        D1 = D1


    mp = np.array([0.5,0.5])

    #checking if C&D lies in the unit circle
    if distance(mp,C1) < (math.sqrt(2)/2) and distance(mp,D1) < (math.sqrt(2)/2):
        return [C1[0],C1[1],D1[0],D1[1]]
    else:
        return 'failed'
