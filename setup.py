from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='django-bootstrap5-dark-mode-switch',
    version='0.2.0',
    packages=[
        'dark_mode_switch',
        'dark_mode_switch.templates.dark_mode_switch',
        'dark_mode_switch.static.dark_mode_switch',
    ],
    include_package_data=True,
    description='Dark mode switch for Django with Bootstrap 5',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Christian Wiegand',
    license='MIT',
    url='https://github.com/christianwgd/django-bootstrap5-dark-mode-switch',
    keywords=['django', 'bootstrap', 'dark mode'],
    install_requires=[
        'django>=4.2',
        'django-bootstrap5>=24.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    zip_safe=False,
)
