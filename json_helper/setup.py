import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pakage-Maleda-Tessema",
    version="0.0.1",
    author="Maleda Tessema",
    author_email="mal.bt27",
    description="Packaging Python Projects walk through",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malbt/PythonFundamentals.Labs.PipModule",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
