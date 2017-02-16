import setuptools

setuptools.setup(
    name='shopify_python',
    version='0.1',
    description='Python Standards Library for Shopify',
    url='http://github.com/shopify/shopify_python',
    author='Shopify Data Acceleration',
    author_email='data-acceleration@shopify.com',
    license='BSD',
    packages=['shopify_python'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 2',
    ],
    test_suite='tests',
    install_requires=[
        'pylint',
        'autopep8',
        'pytest',
    ]
)
