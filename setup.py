# setup.py
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="qstar",
    version="1.0.0",
    author="Guillaume Piron",
    author_email="guizzmop@hotmail.fr",
    description="Q-STAR: Framework IA séquentielle asynchrone et multimodal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guillaume-piron-dev/qstar",
    packages=find_packages(exclude=["tests", "docs", "notebooks"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires=">=3.8",
    install_requires=Path("requirements.txt").read_text(encoding="utf-8").splitlines(),
    entry_points={
        "console_scripts": [
            "qstar=qstar_cli:main"
        ]
    },
)
