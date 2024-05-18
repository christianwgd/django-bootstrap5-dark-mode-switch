import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-bootstrap5-dark-mode-switch',
    version='0.1.0',
    packages=setuptools.find_packages(
        exclude=["dark_mode_switch_sample", "*manage.py",]
    ),
    include_package_data=True,
    description='Dark mode switch for Django with Bootstrap 5',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Christian Wiegand',
    license='MIT',
    url='https://github.com/christianwgd/django-bootstrap5-dark-mode-switch',
    keywords=['django', 'bootstrap', 'dark mode'],
    install_requires=[
        'django',
        'django-bootstrap5'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
