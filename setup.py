from setuptools import setup, find_packages

__version__ = "1.0.0"


# More information on setting these values:
# https://github.com/Sceptre/project/wiki/sceptre-hook-template

# lowercase, use `-` as separator.
HOOK_NAME = 'sceptre-hook-template'
# the hook call in sceptre e.g. !command_name.
HOOK_COMMAND_NAME = 'custom_hook'
HOOK_MODULE_NAME = 'hook.{}'.format(HOOK_COMMAND_NAME)  # do not change.
# CamelCase name of hook class in hook.{HOOK_COMMAND_NAME}.
HOOK_CLASS = 'CustomHook'
HOOK_DESCRIPTION = ''  # one line summary description
# if multiple use a single string with comma separated names.
HOOK_AUTHOR = 'Sceptre'
# if multiple use single string with commas.
HOOK_AUTHOR_EMAIL = 'sceptre@cloudreach.com'
HOOK_URL = 'https://github.com/sceptre/{}'.format(HOOK_NAME)

with open("README.md") as readme_file:
    README = readme_file.read()

install_requirements = [
    "packaging==16.8",
]

test_requirements = [
    "pytest>=3.2",
]

setup_requirements = [
    "pytest-runner>=3"
]

setup(
    name=HOOK_NAME,
    version=__version__,
    description=HOOK_DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=HOOK_AUTHOR,
    author_email=HOOK_AUTHOR_EMAIL,
    license='Apache2',
    url=HOOK_URL,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    py_modules=[HOOK_MODULE_NAME],
    entry_points={
        'sceptre.hooks': [
            "{}={}:{}".format(HOOK_COMMAND_NAME, HOOK_MODULE_NAME, HOOK_CLASS)
        ]
    },
    include_package_data=True,
    zip_safe=False,
    keywords="sceptre, sceptre-hook",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    test_suite="tests",
    install_requires=install_requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    extras_require={
        "test": test_requirements
    }
)
