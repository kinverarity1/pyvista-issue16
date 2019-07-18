# pyvista-issue16

https://github.com/pyvista/pyvista/issues/16

```
(base) kinverarity C:\devapps\projects\pyvista-issue16
$ conda env create -f env.yml
Collecting package metadata (repodata.json): done
Solving environment: done
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pyvista-issue16-0
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) kinverarity C:\devapps\projects\pyvista-issue16
$ conda activate pyvista-issue16-0

(pyvista-issue16-0) kinverarity C:\devapps\projects\pyvista-issue16
$ python test.py
('np.__version__', '1.15.4')
('pv.__version__', '0.21.1')
('pv.ID_TYPE', <class 'numpy.int64'>)
('vertices.dtype', dtype('int32'))
('faces.dtype', dtype('int32'))
Traceback (most recent call last):
  File "test.py", line 24, in <module>
    surf = pv.PolyData(vertices, faces)
  File "c:\devapps\python\anaconda3-32\envs\pyvista-issue16-0\lib\site-packages\pyvista\core\pointset.py", line 123, in __init__
    self._from_arrays(args[0], args[1], deep)
  File "c:\devapps\python\anaconda3-32\envs\pyvista-issue16-0\lib\site-packages\pyvista\core\pointset.py", line 308, in _from_arrays
    self.faces = faces
  File "c:\devapps\python\anaconda3-32\envs\pyvista-issue16-0\lib\site-packages\pyvista\core\pointset.py", line 239, in faces
    vtkcells.SetCells(nfaces, numpy_to_vtkIdTypeArray(faces, deep=False))
  File "c:\devapps\python\anaconda3-32\envs\pyvista-issue16-0\lib\site-packages\vtk\util\numpy_support.py", line 192, in numpy_to_vtkIdTypeArray

    'Expecting a numpy.int32 array, got %s instead.' % (str(dtype)))
ValueError: Expecting a numpy.int32 array, got int64 instead.

(pyvista-issue16-0) C:\devapps\projects\pyvista-issue16
$ conda env export > env-frozen.yml
```