import sys
import math
import numpy as np

# def populate_arr(n):
#     count = 0
#     arr = []
#     while count != n:
#         arr.append(count)
#         count += 1
#     return arr

def combinations(n, c):
    print('combinations:')
    arr = []
    combinationsHelper(n, list(range(n)), c, 0, arr)
    return arr

def combinationsHelper(n, n_arr, c, start, comb_arr): # start: starting index, min: 0
    if n == 0 or c == 0:
        return(comb_arr)
    if start == n-c:
        # print('case 0: start = ' + str(start))
        comb_arr.append(n_arr[start: n])
        return(comb_arr)
    if len(n_arr)-start == c:
        # print('case 1: start = ' + str(start))
        comb_arr.append(n_arr[start:n])
        start += 1
        n_arr = list(range(n))
        combinationsHelper(n, n_arr, c, start, comb_arr)
    else:
        # print('case 2: start = ' + str(start))
        comb_arr.append(n_arr[start:start+c])
        n_arr.pop(start+1)
        combinationsHelper(n, n_arr, c, start, comb_arr)

# theta in degrees
def rot_z(theta, v):
    theta *= math.pi/180
    rot = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ])
    return rot.dot(v)

def rot_y(theta, v):
    theta *= math.pi/180
    rot = np.array([
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ])
    v = np.array(v)
    return rot.dot(v)

def rot_x(theta, v):
    theta *= math.pi/180
    rot = np.array([
        [1,0,0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta),  math.cos(theta)]
    ])
    v = np.array(v)
    return rot.dot(v)

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in degrees between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return 180/math.pi * np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        
if __name__ == "__main__":
    n = (int)(sys.argv[1])
    c = (int)(sys.argv[2])

    for c in combinations(n, c):
        print(c)
    

    
