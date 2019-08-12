from setuptools import setup

with open('README.rst') as file_:
    LONG_DESCRIPTION = file_.read()
with open('VERSION') as version_file:
    version = version_file.read().strip()


setup(name='PyBindGen',
      version=version,
      setup_requires=['setuptools_scm'],
      description='Python Bindings Generator',
      author='Gustavo Carneiro',
      author_email='gjcarneiro@gmail.com',
      url='https://launchpad.net/pybindgen',
      packages=['pybindgen',
                'pybindgen.typehandlers',
                'pybindgen.typehandlers.ctypeparser',
                ],
      long_description=LONG_DESCRIPTION,
      )
