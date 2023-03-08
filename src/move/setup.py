from setuptools import setup, find_packages

package_name = 'move'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    package_data={
    }
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='teus',
    maintainer_email='jt2002120225@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control = move.control:main',
        ],
    },
)
