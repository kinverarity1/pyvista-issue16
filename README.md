# pyvista-issue16

https://github.com/pyvista/pyvista/issues/16

Testing with pyvista PR #316

```
kinverarity@ENVIT C:\devapps\projects\pyvista-issue16
$ conda env create -f env.yml
Collecting package metadata (repodata.json): done
Solving environment: done
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Ran pip subprocess with arguments:
['c:\\devapps\\python\\anaconda3-32\\envs\\pyvista-issue16-pr316\\python.exe', '-m', 'pip', 'install', '-U', '-r', 'C:\\devapps\\projects\\pyvista-issue16\\condaenv.b3cjimsa.requirements.txt']
Pip subprocess output:
Looking in indexes: https://pypi.org/simple, http://envtelem04:8090/simple/
Collecting git+https://github.com/pyvista/pyvista.git@refs/pull/316/head (from -r C:\devapps\projects\pyvista-issue16\condaenv.b3cjimsa.requirements.txt (line 1))
  Cloning https://github.com/pyvista/pyvista.git (to revision refs/pull/316/head) to c:\devapps\temp\pip-req-build-h7239hu1
Requirement not upgraded as not directly required: numpy in c:\devapps\python\anaconda3-32\envs\pyvista-issue16-pr316\lib\site-packages (from pyvista==0.21.1->-r C:\devapps\projects\pyvista-issue16\condaenv.b3cjimsa.requirements.txt (line 1)) (1.16.4)
Collecting imageio (from pyvista==0.21.1->-r C:\devapps\projects\pyvista-issue16\condaenv.b3cjimsa.requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/af/0a/943c965d372dae0b1f1482677d29030ab834351a61a9a632fd62f27f1523/imageio-2.5.0-py3-none-any.whl
Collecting appdirs (from pyvista==0.21.1->-r C:\devapps\projects\pyvista-issue16\condaenv.b3cjimsa.requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/56/eb/810e700ed1349edde4cbdc1b2a21e28cdf115f9faf263f6bbf8447c1abf3/appdirs-1.4.3-py2.py3-none-any.whl
Collecting scooby>=0.2.2 (from pyvista==0.21.1->-r C:\devapps\projects\pyvista-issue16\condaenv.b3cjimsa.requirements.txt (line 1))
Collecting pillow (from imageio->pyvista==0.21.1->-r C:\devapps\projects\pyvista-issue16\condaenv.b3cjimsa.requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/86/00/52d0e56d787c437cd5e6f39929d1ed53b37cbe01280457e29d677b86eceb/Pillow-6.1.0-cp36-cp36m-win32.whl
Building wheels for collected packages: pyvista
  Running setup.py bdist_wheel for pyvista: started
  Running setup.py bdist_wheel for pyvista: finished with status 'done'
  Stored in directory: c:\devapps\temp\pip-ephem-wheel-cache-02dw2l3k\wheels\fc\34\d4\c1a5776572ba15549b2a378c0d4840f54937a44cca6de0c98b
Successfully built pyvista
Installing collected packages: pillow, imageio, appdirs, scooby, pyvista
Successfully installed appdirs-1.4.3 imageio-2.5.0 pillow-6.1.0 pyvista-0.21.1 scooby-0.4.3

#
# To activate this environment, use:
# > activate pyvista-issue16-pr316
#
# To deactivate an active environment, use:
# > deactivate
#
# * for power-users using bash, you must source
#


kinverarity@ENVIT C:\devapps\projects\pyvista-issue16
$ conda activate pyvista-issue16-pr316

(pyvista-issue16-pr316) kinverarity@ENVIT C:\devapps\projects\pyvista-issue16
$ python test.py
('np.__version__', '1.16.4')
('pv.__version__', '0.21.1')
('pv.ID_TYPE', <class 'numpy.int32'>)
('vertices.dtype', dtype('int32'))
('faces.dtype', dtype('int32'))

(pyvista-issue16-pr316) kinverarity@ENVIT C:\devapps\projects\pyvista-issue16
$ conda env export > env-frozen.yml

```