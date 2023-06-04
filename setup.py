from setuptools import setup, find_packages

setup(
    name='Project-gpt',
    version='0.1.0',
    url='https://github.com/Ari1009/project-gpt',
    author='Ari1009',
    author_email='arihant0pal@gmail.com',
    description='Automate your project readme',
    packages=find_packages(),    
    install_requires=['openai', 'python-dotenv'],
    entry_points={
        'console_scripts': [
            'project-gpt = project-gpt:main',
        ],
    },
)

