from setuptools import setup

setup(
    name='androidtv',
    version='0.0.2',
    description='Communicate with an Android TV device via ADB over a network.',
    url='https://github.com/JeffLIrion/python-androidtv/',
    license='MIT',
    author='Jeff Irion',
    author_email='jefflirion@users.noreply.github.com',
    packages=['androidtv'],
    install_requires=['pycryptodome', 'rsa', 'adb-homeassistant'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
