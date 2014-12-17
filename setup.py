from setuptools import setup, find_packages
import subprocess

git_version = subprocess.check_output(["git", "describe", "--tags"]).rstrip()

setup(
    name="annotate-influxdb",
    version=git_version,
    packages=find_packages(),
    scripts=[
        'send-annotation',
    ],
    description='Send annotation to InfluxDB',
    author='Daniel Podlejski',
    author_email='daniel.podlejski@gmail.com',
    platforms=['any'],
    zip_safe=False,
    long_description='Write annotations (http://grafana.org/docs/features/annotations/) into InfluxDB',
    install_requires=[
        'click==3.3',
        'influxdb==0.1.13',
    ],
)
