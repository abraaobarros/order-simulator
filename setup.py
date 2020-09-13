from setuptools import setup
setup(
    name='ckitchen',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'ckitchen=main:cli'
        ]
    }
)
