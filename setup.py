from setuptools import setup

setup(
    name='pysync',
    version='0.1',
    url='https://github.com/izaac/pysync',
    license='MIT',
    author='Izaac Zavaleta',
    author_email='jorge.izaac@gmail.com',
    description='Convert a given date to UTC time',
    test_suite='autogmailpy.tests',
    install_requires=['pytz', 'docopt'],
    scripts=['pysync'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)