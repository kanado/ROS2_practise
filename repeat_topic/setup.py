from setuptools import setup

package_name = 'repeat_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kanade',
    maintainer_email='kanade@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'repeat_publisher_node = repeat_topic.repeat_publisher_node:main',
            'repeat_subscriber_node = repeat_topic.repeat_subscriber_node:main'
        ],
    },
)
