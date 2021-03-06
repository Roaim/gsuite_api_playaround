from setuptools import find_packages, setup

setup(
    name='app',
    version='1.1.3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'click', 'flask_cors', 'flask_sqlalchemy', 'flask_marshmallow', 'marshmallow-sqlalchemy',
        'marshmallow_enum', 'marshmallow', 'flask_migrate', 'werkzeug', 'flask_jwt_extended', 'google-auth-httplib2',
        'google-api-python-client', 'google-auth-oauthlib'
    ]
)
