from setuptools import find_packages, setup

package_name = 'distance_sensor'

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
    maintainer='mkmk',
    maintainer_email='mkmk@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
 entry_points={
    'console_scripts': [
        'publisher = distance_sensor.publisher:main',
        'subscriber = distance_sensor.subscriber:main',
    ],
},
)
