from setuptools import setup, find_packages

setup(
    name="gsa",
    version="0.0.1",
    packages=find_packages(),

    install_requires=[
        "Flask==1.1.2",
        "Flask-Cors==3.0.9",
        "Flask-SocketIO==3.3.1",
    ],
    url="https://github.com/ielm/gsa",
    author="Ivan Leon",
    author_email="leoni@rpi.edu",
    description="GATOR Semantic Annotator Service",
    keywords="annotation",
    project_urls={
        "Documentation": "https://github.com/ielm/gsa",
        "Source Code": "https://github.com/ielm/gsa",
    }
)
