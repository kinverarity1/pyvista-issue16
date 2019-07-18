import numpy as np
print(("np.__version__", np.__version__))

import pyvista as pv
print(("pv.__version__", pv.__version__))

print(("pv.ID_TYPE", pv.ID_TYPE))

# mesh points
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
             [0.5, 0.5, -1]], dtype=np.int32)

# mesh faces
faces = np.hstack([[4, 0, 1, 2, 3],  # square
                   [3, 0, 1, 4],     # triangle
                   [3, 1, 2, 4]])    # triangle

print(("vertices.dtype", vertices.dtype))
print(("faces.dtype", faces.dtype))

surf = pv.PolyData(vertices, faces)

# plot each face with a different color
surf.plot(scalars=np.arange(3), cpos=[-1, 1, 0.5])