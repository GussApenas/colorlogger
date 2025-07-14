from setuptools import setup, find_packages

setup(
    name='colorlogger',
    version='1.0.0',
    description='Logger colorido, contextual e simples para Python',
    author='Guss',
    author_email='agussdevoficial@gmail.com',
    url='https://github.com/GussApenas/colorlogger',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='logger terminal color debug log',
    license='MIT',
)
