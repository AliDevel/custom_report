from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_report/__init__.py
from custom_report import __version__ as version

setup(
	name="custom_report",
	version=version,
	description="Custom Report",
	author="Umer",
	author_email="farooqx2560@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
