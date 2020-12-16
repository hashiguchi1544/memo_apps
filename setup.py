from setuptools import setup, find_packages

setup(
    # パッケージに関するメタ情報を記述
    name='mycmd',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='hashiguchi1544',
    author_email='hashiguhci1544@example.com',
    description='',

    # https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=entry_points#entry-points
    entry_points={'console_scripts': ['memo=main:main']}
)