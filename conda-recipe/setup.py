from setuptools import *
from pathlib import Path

with open(Path(__file__ ).parent / '../README.md', 'r', encoding='utf-8') as fh:
	long_description= fh.read()


setup(
    name = "cptdl",
    version = "1.0.6",
    author = "Kyle Hall",
    author_email = "pycpt-help@iri.columbia.edu",
    description = ("Tools bridging Xarray and CPT"),
    license = "MIT",
    keywords = ["climate", 'predictability', 'prediction', 'precipitation', 'temperature', 'data', 'IRI', 'DL'],
    url = "https://iri.columbia.edu/our-expertise/climate/tools/",
    packages=[  'cptdl',  ],
	package_dir={ 'cptdl': Path(__file__ ).parent / '../src',                },
	python_requires=">=3.0",
    long_description=long_description,
	long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
    ],
)
