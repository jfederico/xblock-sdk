"""Setup for {{cookiecutter.short_name|lower}} XBlock."""

import os
from setuptools import setup


def get_package_data(package, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `package`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(package, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), package))

    return {package: data}


setup(
    name='{{cookiecutter.short_name|lower}}-xblock',
    version='0.1',
    description='{{cookiecutter.short_name|lower}} XBlock',   # TODO: write a better description.
    packages=[
        '{{cookiecutter.short_name|lower}}',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            '{{cookiecutter.short_name|lower}} = {{cookiecutter.short_name|lower}}:{{cookiecutter.class_name}}',
        ]
    },
    package_data=get_package_data("{{cookiecutter.short_name|lower}}", ["private", "public"]),
)
