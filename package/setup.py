from setuptools import setup

# List of dependenies installed via `pip install -e .`
# by virtue ofthe Setuptools `install_requires` value below.
requires = [
    'pyramid',
    'waitress',
]

setup(
    name='tutorial',
    install_requires=requires,
)

