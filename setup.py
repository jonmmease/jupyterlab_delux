# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from setuptools import setup

setup_args = dict(
    name             = 'jupyterlab_delux',
    description      = 'A proof-of-concept build of JupyterLab with the ipywidgets and bqplot extensions preinstalled',
    version          = '0.2',
    packages         = ['jupyterlab_delux', ],
    entry_points     = {'console_scripts': [
                            'delux-lab = jupyterlab_delux.labapp:main',
                            'delux-labextension = jupyterlab_delux.labextensionapp:main',
                        ]},
    author           = 'Jupyter Development Team',
    url              = 'https://github.com/measejm1/jupyterlab_delux',
    license          = 'BSD',
    platforms        = "Linux, Mac OS X, Windows",
    keywords         = ['ipython', 'jupyterlab', 'jupyter', 'Web'],
    classifiers      = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

setup(**setup_args)
