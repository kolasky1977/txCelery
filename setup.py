#!/usr/bin/env python
from setuptools import setup


package_name = 'txcelery'
package_version = '1.2.0'

setup(
    name='txcelery-py3',
    provides='txcelery',
    version=package_version,
    author='Sentimens Research Group, LLC',
    author_email='contact@sentimens.com',
    maintainer="Sentimens Research Group, LLC",
    maintainer_email="contact@sentimens.com",
    packages=['txcelery'],
    include_package_data=True,
    install_requires=['Twisted>=11.0.0', 'Celery>=3.0.0', 'setuptools>=0.6'],
    url='https://github.com/SentimensRG/txCelery',
    license='MIT',
    description=('Celery for Twisted:  manage Celery tasks from twisted'
                 'using the Deferred API'),
    keywords=["celery", "twisted", "deferred", "async", "asynchronous"],
    long_description="""Celery for Twisted:
    Manage Celery tasks from twisted using the Deferred API""",
    classifiers=[
        "Programming Language :: Python :: 3.5",
    ],
)
