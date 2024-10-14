from setuptools import setup, find_packages

setup(
    name='NormLatexStr',
    version='0.1.1',
    author='Achille Merendino',
    author_email='achille@achilleme.com',
    description='A package to format numbers with their uncertainties in LaTeX using the SIunitx package.',
    packages=find_packages(),
    install_requires=[
        'math'
    ]
)

