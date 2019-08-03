from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    README = f.read()

setup(
    name='asproxy',
    version='0.1.0',
    description='Simple HTTP proxy.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/nnnewb/asproxy',
    author='weak_ptr',
    author_email='weak_ptr@163.com',
    classifier=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='proxy asyncio',
    packages=find_packages(),
    python_requires='>= 3.6',
    install_requires=[
        'aiohttp==3.5.4',
        'coloredlogs==10.0',
    ],
    entry_points={
        'console_scripts': [
            'asproxy = asproxy.cli:main',
        ],
    }
)
