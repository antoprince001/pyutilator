import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pyutilator",
    version = "0.0.2",
    author = "Antony Prince J",
    author_email = "antoprince001@gmail.com",
    description = "Python Utility Decorators",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/antoprince001/pyutilator",
    # project_urls = {
    #     "Bug Tracker": "package issues URL",
    # },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)
