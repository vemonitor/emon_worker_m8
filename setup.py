"""EmonCmsWorker Setup"""
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='emon_worker_m8',
    version='0.0.1',
    description='VeMonitor_m8 EmonCmsWorker Package',
    url='https://github.com/vemonitor/emon_worker_m8',
    author='Eli Serra',
    author_email='eli.serra173@gmail.com',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    license='Apache',
    packages=['test', 'emon_worker_m8'],
    package_dir={
        'emon_worker_m8': 'emon_worker_m8',
        'test': 'test'
    },
    install_requires=[
        'requests',
        'vemonitor_m8',
        've_utils',
    ],
    extras_require={
        "TEST": [
            "pytest>=7.1.2",
            "coverage",
            "pytest-cov"
        ]
    },
    python_requires='>3.7.0',
    zip_safe=False
)
