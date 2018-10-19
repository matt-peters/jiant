#!/usr/bin/python
import setuptools

setuptools.setup(
    name='jiant',
    version='0.1',
    packages=['jiant', 'jiant.allennlp_mods', 'jiant.cnns', 'jiant.cove',
              'jiant.openai_transformer_lm'],
    package_dir={'jiant': 'src'},
    tests_require=[],
    zip_safe=False,
    entry_points='',
)

