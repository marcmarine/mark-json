from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
    name="mark_json",
    version="0.1.1",
    description='Converts Markdown to a structured JSON format, ideal for long documents',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/marcmarine/mark-json',
    author='Marc Mariné',
    author_email='shenobi@gmail.com',
    license='LICENSE',
    keywords='markdown md json parser syntax tree',
    packages=find_packages(),
    install_requires=[
      'PyYAML==6.0.2'
    ]
)