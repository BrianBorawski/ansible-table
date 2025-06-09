from setuptools import setup, find_packages

setup(
    name='ansible_hive_module',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyodbc>=4.0.30',
        'requests>=2.25.1',
        'ansible>=2.9'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='Ansible module for managing Hive tables and databases via ODBC or REST',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
    ],
)
