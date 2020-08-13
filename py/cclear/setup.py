from setuptools import setup

'''
python setup.py sdist
pip install dist/cclear-0.1.0.tar.gz
'''

setup(
    name='cclear',
    py_modules=['cclear'],
    version='0.1.0',
    license='BSD',
    entry_points={
        'console_scripts': [
            'cc = cclear:cclear',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
