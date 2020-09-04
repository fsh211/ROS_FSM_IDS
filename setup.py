from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup


d = generate_distutils_setup()
d['packages'] = ['fsm_ids']
d['package_dir'] = {'': 'src'}

setup(**d)


# need to uncomment catkin_python_setup() in CMakeLists.txt to work