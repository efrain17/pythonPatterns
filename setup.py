from setuptools import setup

setup(
    name='pip_pattern',
    version='0.1',
    py_modules=['sv'],
    install_requires=[
        'pytest',
        'pytest-cov',
        'pytest-mock',
        'pytest-watch',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
