import numpy as np
def closest(atoms, v, r):
  v_coords = atoms[v]
  count = 0
  for k in range(len(atoms)):
    if k != v:  
      k_coords = atoms[k]
      distance = np.linalg.norm(np.array(v_coords) - np.array(k_coords))
      if distance < r:
        count += 1
  return count

atoms = np.array(
 [
 [1.0, 0.0, 2.0],
 [-1.0, 0.5, 2.0],
 [-2.0, 1.5, 0.0],
 [2.5, -1.2, -0.5],
 [1.5, 0.2, -0.2]
 ])

v = 1
r = 2.5  

num_closest = closest(atoms, v, r)
print(num_closest)