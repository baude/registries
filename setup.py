import setuptools
#from distutils.core import setup
#install_requires=["PyYAML", "python2-pytoml"],
#    packages=["registries"],
setuptools.setup(
    name='registries',
    version="0.1",
    description='registry parser',
    author='Brent Baude',
    author_email='bbaude@redhat.com',
    url='http://github.com:projectatomic/registries',
    packages=['registries'],
    license='GNU GPL',
    entry_points={
        'console_scripts': [
            'registries = registries.registries:registries'
        ]
    }
)

