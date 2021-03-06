import setuptools


with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='graham',
    use_scm_version={'version_scheme': 'post-release'},
    description="Graham, making s'mores with attrs and marshmallow.",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Kyle Altendorf',
    author_email='sda@fstab.net',
    url='https://github.com/altendky/graham',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            (
                'graham_update_gitignore'
                '= graham.cli.updategitignore:cli'
                '[gitignore]'
            ),
        ],
    },
    install_requires=[
        'attrs',
        'marshmallow',
    ],
    extras_require={
        'docs': [
            'sphinx',
            'sphinx-issues'
        ],
        'tests': [
            'codecov',
            'pytest',
            'pytest-cov',
            'tox',
        ],
        'gitignore': [
            'click',
            'requests',
        ],
    },
    setup_requires=[
        'setuptools_scm',
    ],
)
