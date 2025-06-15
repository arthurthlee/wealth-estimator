from setuptools import setup, find_packages

with open("requirements/prd.txt", encoding="utf-8") as f:
    DEPENDENCIES = f.read().splitlines()

EXCLUDED_PACKAGES = ['tests.*']

setup(
    name="wealth_estimator_api",
    version="0.1.0",
    author="Arthur Lee",
    author_email="arthurthlee@gmail.com",
    description="An API that estimates net worth from a selfie and finds visually similar wealthy individuals.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arthurthlee/wealth-estimator-api",  # update this
    packages=find_packages(exclude=EXCLUDED_PACKAGES),
    include_package_data=True,
    install_requires=[DEPENDENCIES],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
