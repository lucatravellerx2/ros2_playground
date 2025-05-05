from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'python_playground'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*_launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lucatravellerx2',
    maintainer_email='lucatraveller.x2.lightwaves@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tester_node = python_playground.tester_node:main',
            "service_node = python_playground.service_node:main",
            "logger_node = python_playground.logger_node:main",
            "inter_node = python_playground.interface_white_list:main"
        ],
    },
)
