from setuptools import setup

setup(
    name = 'simple_cli',
    version='0.0.1',
    py_modules=["simple_cli"],
    entry_points={
        'console_scripts': [
            'simple_cli=simple_cli:main',
        ]
    }
)
