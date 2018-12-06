from pathlib import Path

from setuptools import setup


def readme():
    return Path('README.md').read_text()


setup(name='flask_joke',
      version='0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://github.com/cassiobotaro/flask_joke',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      install_requires=[
          'markdown',
          'flask',
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      scripts=['bin/funniest-joke'],
      entry_points={
          'console_scripts': ['funniest-joke-cli=flask_joke.cli:main'],
      },
      include_package_data=True,
      packages=['flask_joke'],
      zip_safe=False)
