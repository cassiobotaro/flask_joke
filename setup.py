from setuptools import setup

setup(name='flask_joke',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/cassiobotaro/flask_joke',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      install_requires=[
          'markdown',
      ],
      packages=['flask_joke'],
      zip_safe=False)
