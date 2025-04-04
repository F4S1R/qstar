# setup.py
from setuptools import setup, find_packages

setup(
    name="qstar",
    version="1.0.0",
    author="Guillaume Piron",
    description="Q-STAR: Framework IA séquentielle asynchrone et multimodal.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/guillaume-piron-dev/qstar",
    packages=find_packages(exclude=["tests", "docs", "notebooks"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires=">=3.8",
    install_requires=open("requirements.txt").read().splitlines(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "qstar=qstar_cli:main"
        ]
    },
)


# pyproject.toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"


# MANIFEST.in
include README.md
include requirements.txt
include LICENSE.md
include Makefile
include setup.py
include run.py
include run_all.sh
include qstar_cli.py
recursive-include qstar *
recursive-include api *
recursive-include agents *
recursive-include bindings *
recursive-include config *
recursive-include deployment *
recursive-include docker *
recursive-include docs *
recursive-include edge *
recursive-include examples *
recursive-include hardware *
recursive-include modules *
recursive-include profile *
recursive-include reinforcement *
recursive-include scripts *
recursive-include security *
recursive-include tests *
recursive-include tools *
recursive-include train *
recursive-include outputs *
recursive-include datasets *
recursive-include notebooks *
recursive-include .github *
