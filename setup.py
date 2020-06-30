import setuptools

setuptools.setup(
    name='mac-tag-sync',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/tag-sync']
)
