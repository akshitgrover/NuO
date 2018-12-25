from distutils.core import setup
import codecs

import NuO

setup (

    name = "NuO",
    version = "0.1.9",
    author = "Akshit Grover",
    author_email = "akshit.grover2016@gmail.com",
    description = "Static website templating engine, Generates HTML pages using .nuo template files and data in JSON files.",
    packages = [
        "NuO",
        "NuO.configParser",
        "NuO.dataInterface",
        "NuO.nuoParser",
        "NuO.nuoParser.handlers"
    ],
    long_description = open("README.rst").read(),
    entry_points={
        "console_scripts": [
            "nuo = NuO.nuo:main",
            "NuO = NuO.nuo:main"
        ]
    },
    install_requires = [
        "PyYAML"
    ],
    license = "LICENSE",
    url = "https://github.com/akshitgrover/NuO",
    keywords = "static html website parser nuo",
    classifiers = [

        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    
    ]

)