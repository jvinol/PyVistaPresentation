import pyvista as pv

# visualize built-in geometry
mesh = pv.examples.load_sphere()
mesh.plot()

print(type(mesh)) # "PolyData" class stores geometry

# # or read STL files
# mesh = pv.read('Standard Bottle.STL')
# mesh.plot()

# # add some useful kwargs for formatting
# mesh = pv.read('Standard Bottle.STL')
# mesh.plot(parallel_projection=True,
# 	show_edges=True,
# 	background='white’)


# # color the bottle by its mesh quality
# mesh = pv.read('Standard Bottle.STL')
# mesh_quality = mesh.compute_cell_quality()
# mesh_quality.plot(scalars='CellQuality', show_edges=True)

# # use updated file with more uniform mesh
# mesh = pv.read('Standard Bottle 2.STL')
# mesh_quality = mesh.compute_cell_quality()
# mesh_quality.plot(scalars='CellQuality', show_edges=True)
