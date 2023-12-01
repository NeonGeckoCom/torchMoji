from setuptools import setup

setup(
    name='torchmoji',
    version='1.0',
    packages=['torchmoji'],
    description='torchMoji',
    include_package_data=True,
    install_requires=[
        'emoji~=0.4',
        'numpy~=1.18',
        'scipy~=1.5',
        'scikit-learn~=0.19',
        'text-unidecode==1.0',
        'nose~=1.3.7',
        'torch~=1.7.1'
    ],
)
