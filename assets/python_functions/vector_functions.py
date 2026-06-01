import numpy as np

def getAngle(v1, v2):
    '''
    Calculate the angle between two vectors.

    Parameters:
        v1 (numpy.array): The first vector.
        v2 (numpy.array): The second vector.

    Returns:
        float: The calculated angle.
    '''
    rad=np.arccos(np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)))
    angle=rad*(180/np.pi)
    return angle

def rotate(v1, v2, norm, angl):
    '''
    Take two vectors and rotate the first one around a given line, the second one gets rotated in the same manner, so that both vectors keep their angle to each other.

    Parameters:
        v1 (numpy.array): The first vector.
        v2 (numpy.array): The second vector.
        norm (numpy.array): A vector that represents the direction of a line. vec1/vec2 will be rotated around this line.
        angl (numpy.array): A given angle that defines about how many degrees both vectors gets rotated

    Returns:
        tuple:
            - numpy.array -- The rotated first vector.
            - numpy.array -- The rotated second vector.
    '''
    nx,ny,nz = norm
    r1 = [nx*nx*(1-np.cos(angl)) + np.cos(angl),
        nx*ny*(1-np.cos(angl)) - nz * np.sin(angl),
        nx*nz*(1-np.cos(angl)) + ny * np.sin(angl)]

    r2 = [ny*nx*(1-np.cos(angl)) + nz * np.sin(angl),
        ny*ny*(1-np.cos(angl)) + np.cos(angl),
        ny*nz*(1-np.cos(angl)) - nx * np.sin(angl)]

    r3 = [nz*nx*(1-np.cos(angl)) - ny * np.sin(angl),
        nz*ny*(1-np.cos(angl)) + nx * np.sin(angl),
        nz*nz*(1-np.cos(angl)) + np.cos(angl)]

    mat = (r1,r2,r3)

    return np.matmul(v1, mat), np.matmul(v2, mat)

def transform(v1, v2):
    '''
    Take two vectors as input and rotate the second vector, so that it has the same angle to the z-unitvector as the first vector to the second one.

    Parameters: 
        v1 (numpy.array): The first vector.
        v2 (numpy.array): The second vector.

    Returns: 
        numpy.array: The rotated second vector.
    '''
    # create normal vector of v1 and z-unitvector
    n = np.cross(v1, (0,0,1))
    n1,n2,n3 = n
    n = n / np.sqrt(n1*n1 + n2*n2 + n3*n3) # normalize normal vector

    a = getAngle((0,0,1),v1)

    r1,r2 = rotate(v1,v2,n,-np.radians(a))

    return r2

def getAspect(normal):
    '''
    Calculate the aspect of a given vector.

    Parameters: 
        normal: The vector whose aspect should be returned.

    Returns:
        float: The calculated aspect.
    '''
    nx,ny,nz=normal

    a = 0.0
    b = 0.0
    a = float(0.0 * nx + 1.0 * ny)

    b = float(np.sqrt(nx * nx + ny * ny) * 1)
    cn = 0.0

    if b == 0.0:
        cn=0.0
    else:
        cn=((np.arccos(a/b)*180.0)/np.pi)
        if nx < 0.0:
            cn = 360.0 - cn

    return cn

def getSlope(normal):
    '''
    Calculate the slope of a given vector.

    Parameters: 
        normal: The vector whose slope should be returned.

    Returns:
        float: The calculated slope.
    '''
    nx,ny,nz=normal

    dx = float(np.sqrt(nx * nx + ny * ny))
    dy = float(nz)
    c = 0.0

    if dx == 0.0:
        c=0.0
    else:
        c=abs(np.arctan(dy/dx))*180.0/np.pi
        c=90.0-c

    return c