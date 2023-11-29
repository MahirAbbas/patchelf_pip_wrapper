from setuptools import setup, find_packages

setup(
    name='patchelf_pip_wrapper',
    version='0.1',
    packages=find_packages(),
    description='Python wrapper for patchelf',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mahirabbas/patchelf_wrapper',
    author='Mahir Abbas',
    author_email='mabbasest@outlook.com',
    license='MIT',
    install_requires=[
        # Any dependencies, if you have them
    ],
    classifiers=[
        # Classifiers help categorize the project on PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

