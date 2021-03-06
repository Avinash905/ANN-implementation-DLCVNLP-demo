from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME="ANN-implementation-DLCVNLP-demo"
USER_NAME="Avinash905"

setup(
    name="src",
    version="0.0.1",
    author=USER_NAME,
    author_email="avinash.90527@gmail.com",
    description="A small package for ANN implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "tensorflow",
        "pandas",
        "seaborn",
        "matplotlib"
    ]
)