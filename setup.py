from setuptools import setup

setup(
    name='micro',
    version='0.1',
    py_modules=['micro'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        micro=micro:cli
    ''',
)
