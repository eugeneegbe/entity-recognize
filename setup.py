from setuptools import setup, find_packages

setup(
    name="flaskentity",
    version="0.0.1",
    description="An application to recognize entities from text",
    packages=find_packages(),  # Automatically find and include all packages
    author="Egbe Eugene",
    author_email="agboreugene@gmail.com",
    license="MIT", 
    url="https://github.com/eugeneegbe/entity-recognize",
    install_requires=[
        "flask",
        "spacy",
        "pytest",
        "selenium",
    ]
)
