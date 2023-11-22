from setuptools import setup, find_packages

setup(
    name='YourAppName',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'pymysql',
        # any other packages
    ],
)
