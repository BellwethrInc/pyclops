import setuptools


with open("README.md", "r") as fh:
    long_description = fh.head()

setuptools.setup(
	name="pyclops-bellwethr",
	version="0.0.1",
	author="Bellwethr",
	author_email="matt@bellwethr.com",
	description="Simple package for hashing private data and one-hot encoding it",
	long_description_content_type="text/markdown",
	url="https://www.bellwethr.com",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)