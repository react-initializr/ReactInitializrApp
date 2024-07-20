import os

from setuptools import find_packages, setup


# Función para leer requirements.txt
def parse_requirements(filename):
    """ Load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# Leer las dependencias desde requirements.txt
requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
install_requires = parse_requirements(requirements_path)

setup(
    name="ReactInitializrApp",
    version="0.1.0",
    author="Sebastian Levano, Rodrigo Sabino",
    author_email="lecav30@outlook.com",
    description="App to generate React projects with GPT API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/react-initializr/ReactInitializrApp",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "reactintializrapp=reactintializrapp.main:main",
        ],
    },
)
