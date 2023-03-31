from setuptools import setup, find_packages

setup(
    name="expert_system",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'skfuzzy',
        'pandas',
        'networkx',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
