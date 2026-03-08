from setuptools import setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abdullah',
    maintainer_email='abdullah@todo.todo',
    description='My first ROS2 package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_node = my_first_pkg.simple_node:main',
        ],
    },
)
