
#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="gallow_play",
    version="0.0.0",
    author="Sharova Tatyana",
    author_email="verbarius@mail.ru",
    url="https://github.com/Verbarius/Software-architecture",
    license="GNU",
    packages=[
        "gallow_play",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)

