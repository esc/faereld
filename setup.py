# -*- coding: utf-8 -*-

from setuptools import setup

try:
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
except IOError:
    readme = ''


setup(
    name='faereld',
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    description='Time tracking tool',
    long_description=readme,
    entry_points={
        'console_scripts': [
            'faereld = faereld.__main__:main',
        ]
    },
    packages=['faereld'],
    install_requires=[
        'PyYAML==3.13',
        'datarum==0.5.0',
        'wisdomhord==0.2.4',
        'numpy==1.15.0',
        'prompt-toolkit==1.0.15'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    use_scm_version=True
)
