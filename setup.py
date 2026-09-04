from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as file:
        return file.read()


setup(
    name="images-into-array",
    version="3.0.0",
    description="Convert multiple images into NumPy arrays and different color spaces",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sujitmandal/images-into-array",
    author="Sujit Mandal",
    author_email="mandals974@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "opencv-python",
        "tqdm",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    include_package_data=True,
)
