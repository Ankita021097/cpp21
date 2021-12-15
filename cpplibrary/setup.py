import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="example-pkg-totaljacketscpp",
# Replace with your own username above
    version="0.0.2",
    author="AnkitaParande",
    author_email="ankitaparande0210@gmail.com",
    description="To calculate the total",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
# if you have libraries that your module/package/librarys
#you would include them in the install_requires argument
install_requires=[''],
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires='>=3.6',
)