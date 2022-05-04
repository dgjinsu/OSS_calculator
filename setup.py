import setuptools

setuptools.setup (
	include_package_data= True,
	name = 'jscalculator',
	version='1.0.0',
	description='oss_jinsu_calculator',
	author='dgjinsu',
	author_email='1923915@donga.ac.kr',
	url="https://github.com/dgjinsu/OSS_calculator.git",
	download_url='https://github.com/dgjinsu/OSS_calculator/archive/refs/tags/1.0.0.zip',
	install_requires = ['pytest'],
	long_description='oss-dev calculator python module',
	long_description_content_type = 'text/markdown',
	classifiers=
	[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
