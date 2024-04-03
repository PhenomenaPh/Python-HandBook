import math
import numpy as np

coord_1 = np.array(list(map(float, input().split())))
rad, t = list(map(float, input().split()))

coord_2 = np.array([rad * math.cos(t), rad * math.sin(t)])

distance = np.linalg.norm(coord_1 - coord_2)

print(distance)
