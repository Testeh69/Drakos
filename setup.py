from setuptools import setup, find_packages

setup(
    name="drakos",
    version="0.1",
    packages=find_packages(where="."),  # recherche dans ./drakos/
    install_requires=[
        "typer",
        "pandas",
        "numpy",
        "matplotlib",
        
        "scikit-learn",
        "statsmodels", 
        "rich"],
    entry_points={
        "console_scripts": [
            "drk=main:app"
        ]
    },
)