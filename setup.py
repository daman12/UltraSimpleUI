import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UltraSimpleUI", # Replace with your own username
    version="0.0.1",
    description="A package for making UI easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daman12/UltraSimpleUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
