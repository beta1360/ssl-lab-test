from setuptools import setup, find_packages

setup(
    name            = "ssllabtest",
    version         = "1.0.0",
    description     = "SSL-Seminar-test repository:: Topic - Package Test and Deployment",
    author          = "Keon-Hee Lee",
    author_email    = "beta1360@naver.com",
    url             = "https://github.com/KeonHeeLee/ssl-lab-test",
    download_url    = "https://github.com/KeonHeeLee/ssl-lab-test/archive/v1.0.0.tar.gz",
    install_requires= [],
    packages        = find_packages(exclude=['test']),
    keywords        = ['Test', 'TDD', 'Deployment', 'Seminar'],
    python_requires = '>=3',
    zip_safe        = False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)