from setuptools import setup, find_packages

setup(
    name="quantbets",
    version="0.1.0",
    author="Andreas Pappas",
    author_email="your.email@example.com",
    description="A package for quantitative betting analysis.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/itsDreDev/quantbets",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Your package dependencies here. For example:
        'numpy>=1.18.0',
        # 'pandas>=1.0.0',
    ],
    extras_require={
        'dev': [
            'black==21.5b1',
            'flake8==3.9.0',
            'pytest==6.2.4',
            # Any other additional packages for development
        ],
    },
)
