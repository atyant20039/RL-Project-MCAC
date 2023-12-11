from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 7, \
    "You should have Python 3.7 and greater." 

setup(
    name='mcac',
    py_modules=['mcac'],
    version='0.0.1',
    install_requires=[
        'numpy',
        'gym',
        'joblib',
        'matplotlib',
        'torch',
        'tqdm',
        'moviepy',
        'opencv-python',
        'torchvision',
        'dotmap',
        'scikit-image',
        'mujoco-py',
        'robosuite',

    ],
    description="Code for Monte Carlo Augmented Actor Critic.",
    author="Albert Wilcox",
)
