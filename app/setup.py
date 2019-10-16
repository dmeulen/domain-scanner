from setuptools import setup

setup(
    name='domain scanner',
    version='0.0.1',
    packages=['dnsalert'],
    url='',
    license='MIT',
    author='Danny van der Meulen',
    author_email='danny@catdevbrain.nl',
    install_requires=[
        'flask',
        'dnspython',
        'checkdmarc',
        'gunicorn',
        'elasticsearch'
    ]
)
