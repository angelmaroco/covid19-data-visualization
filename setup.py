from setuptools import setup

setup(
    name='covid19-statistics',
    version='0.0.1',
    description='Covid19 visualizations',
    url='https://github.com/degaleon/covid19-statistics',
    author='degaleon',
    author_email='degaleon@gmail.com',
    license='GNU GPLv3',
    zip_safe=False,
    include_package_data=True,
    package_data={
        '': ['*.*']
    },
    install_requires=[
        'numpy>=1.18.4',
        'scipy>=1.4.1 ',
        'pandas>=1.0.3',
        'seaborn>=0.10.1',
        'xlrd2>=1.2.3',
        'osmnx>=0.12.1',
        'networkx>=2.4',
        'descartes>=1.1.0',
        'Unidecode>=1.1.1',
        'folium>=0.11.0',
        'pyepsg>=0.4.0',
        'openpyxl>=3.0.3',
        'jupyter>=1.0.0',
        'jupyter-core>=4.6.3',
        'notebook>=6.0.3',
        'jupyter_contrib_nbextensions>=0.5.1',
        'jupyter_tabnine>=1.1.0',
        'plotly-express>=0.4.1',
        'chart-studio>=1.1.0',
        'psutil>=5.7.0',
        'ipykernel>=5.2.1',
        'Shapely>=1.7.0'
    ],
)
