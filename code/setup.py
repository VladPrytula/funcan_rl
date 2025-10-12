from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rl-toolkit",
    version="0.1.0",
    author="Jean-Pierre Dubois, Max Rubin",
    author_email="noreply@example.com",
    description="Reinforcement Learning from Theory to Practice: Companion Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rl-toolkit",  # Update with actual URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "torch>=2.0.0",
        "matplotlib>=3.7.0",
        "flask>=2.3.0",
        "flask-cors>=4.0.0",
        "pytest>=7.4.0",
        "tqdm>=4.65.0",
    ],
    extras_require={
        "jax": ["jax>=0.4.0", "jaxlib>=0.4.0"],
        "viz": ["seaborn>=0.12.0", "pygame>=2.5.0"],
        "dev": [
            "pytest-cov>=4.1.0",
            "mypy>=1.4.0",
            "black>=23.7.0",
        ],
        "tracking": [
            "tensorboard>=2.13.0",
            "wandb>=0.15.0",
        ],
    },
    entry_points={
        "console_scripts": [
            # Add command-line tools here if needed
            # "rl-train=rl_toolkit.cli:train",
        ],
    },
)
