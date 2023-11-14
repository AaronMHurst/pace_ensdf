#!/bin/bash

# Script to remove folders created during package-building process.
# Uninstalls paceENSDF package, then re-installs it.
# Run this script after editing source modules in the paceENSDF package.

rm -rf build
rm -rf dist
rm -rf paceENSDF.egg-info

rm -f *~
rm -f paceENSDF/*~
rm -f tests/*~

pip uninstall paceENSDF<<EOF
y
EOF

python setup.py install
