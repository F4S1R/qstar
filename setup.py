from setuptools import setup, find_packages
from pathlib import Path
import re

# Lecture dynamique de la version depuis qstar/__init__.py
def get_version():
    init_path = Path("qstar/__init__.py")
    content = init_path.read_text(encoding="utf-8")
    match = re.search(r'__version__\s*=\s*"(.*?)"', content)
    if not match:
        raise RuntimeError("Impossible de trouver la version dans qstar/__init__.py")
    return match.group(1)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="qstar",
    version=get_version(),
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
    install_requires=[
        # Base
        "numpy>=1.20",
        "transformers>=4.37.2",
        "torch>=2.1.2",
        "torchaudio>=2.1.2",
        "Pillow>=10.1.0",

        # Vision
        "opencv-python",
        "scikit-learn",

        # Audio
        "librosa",

        # API
        "fastapi",
        "uvicorn",

        # Interface
        "gradio",

        # Sécurité & Lint
        "flake8",
        "black",
        "bandit",

        # Test
        "pytest",
        "coverage",

        # RLHF / TRL
        "trl",
        "datasets",

        # Utilitaires
        "pyyaml",
        "rich",

        # Optionnel - JAX / TF
        "jax",
        "ml_dtypes>=0.4.0",
        "tensorflow==2.15.0",
        "tensorboard==2.15.2",
        "keras==2.15.0"
    ],
    entry_points={
        "console_scripts": [
            "qstar=qstar_cli:main"
        ]
    },
    project_urls={
        "Documentation": "https://github.com/guillaume-piron-dev/qstar#readme",
        "Source": "https://github.com/guillaume-piron-dev/qstar",
        "Bug Tracker": "https://github.com/guillaume-piron-dev/qstar/issues"
    },
    scripts=[
        "scripts/install_qstar.bat",
        "scripts/install_qstar.sh"
    ]
)
