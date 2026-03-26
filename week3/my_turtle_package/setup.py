from setuptools import find_packages, setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abdullah',
    maintainer_email='mabdullahasif1104@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'circle_node = my_turtle_package.circle_turtle:main',
            'square_node = my_turtle_package.square_turtle:main',
            'triangle_node = my_turtle_package.triangle_turtle:main',
            'goto_node = my_turtle_package.goto_turtle:main',
        ],
    },
)
