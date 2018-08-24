# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from setuptools import setup

setup_args = dict(
    name             = 'jupyterlab_{{ cookiecutter.project_slug }}',
    description      = '{{ cookiecutter.short_description }}',
    version          = '{{ cookiecutter.version }}',
    packages         = ['jupyterlab_{{ cookiecutter.project_slug }}', ],
    entry_points     = {'console_scripts': [
                            '{{ cookiecutter.project_slug }}-lab = jupyterlab_{{ cookiecutter.project_slug }}.labapp:main',
                            '{{ cookiecutter.project_slug }}-labextension = jupyterlab_{{ cookiecutter.project_slug }}.labextensionapp:main',
                        ]},
    author           = '{{ cookiecutter.full_name }}',
    author_email     = '{{ cookiecutter.email }}',
    url              = 'https://github.com/{{ cookiecutter.github_username }}/jupyterlab_{{ cookiecutter.project_slug }}',
    license          = 'BSD 3-Clause',
    platforms        = "Linux, Mac OS X, Windows",
    keywords         = ['jupyterlab', 'jupyter', 'conda'],
    classifiers      = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

setup(**setup_args)
