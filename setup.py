from distutils.core import setup

DESC = 'An open source Python package for performing, finishing, and analyzing ensemble clustering.'

# Run setup
setup(
    name='OpenEnsembles',
    version='v2.0.0',
    author='Naegle Lab',
    url='https://github.com/NaegleLab/OpenEnsembles',
    packages=['openensembles'],
    install_requires=['networkx==2.5'],
    license='GNU General Public License v3',
    summary=DESC,
    long_description=DESC,
)

