from distutils.core import setup
import os

mods = filter(lambda x: x.endswith(".py") and x != "setup.py", os.listdir("."))
mods += map(lambda x: "gallery_plugins/%s" % x, filter(lambda x: x.endswith(".py"), os.listdir("gallery_plugins")))
mods = map(lambda x: x.replace(".py",""), mods)
setup(name = 'gallery_get',
    version = '1.6.2',
    author = 'Rego Sen',
    author_email = 'regosen@gmail.com',
    url = 'https://github.com/regosen/gallery_get',
    description = 'Gallery downloader - supports many galleries and reddit histories',
    long_description = open("README.rst","r").read(),
    license = 'MIT',
    keywords = 'gallery downloader reddit imgur xhamster',
    py_modules = mods,
    packages=['gallery_plugins'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet',
        'Topic :: Multimedia :: Graphics',
    ],
)