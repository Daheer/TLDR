import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "TLDR"
AUTHOR_USER_NAME = "Daheer"
AUTHOR_EMAIL = "suhayrid6@gmail.com"
SRC_REPO = "TLDR"

setuptools.setup(
  name=SRC_REPO,
  version=__version__,
  author=AUTHOR_USER_NAME,
  author_email=AUTHOR_EMAIL,
  description="Text summarization from the ground up. Model building all the way to deployment.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
  project_urls={
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
  },
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.6",
)
