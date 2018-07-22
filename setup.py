from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name="testcase",
    description="Demonstrates undesirable setuptools behavior.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sopoforic/testcase_01',
    author="Tracy Poff",
    author_email="tracy.poff@gmail.com",
    packages=['testcase',],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    entry_points={
        'console_scripts': [
            'testcase = testcase.app:main',
        ],
    },
)
