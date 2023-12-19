#!/bin/bash

# Script to remove folders created during package-building process.
# Uninstalls paceENSDF package, then re-installs it.
# Run this script after editing source modules in the paceENSDF package.

# Function to display script usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "-h, --help       Display this help message."
    echo "-r, --regular    Use decay datasets from ENSDF with regular intensities."
    echo "-t, --transient  Use decay datasest from ENSDF with transient equilibrium intensities."
}

# Specify directory locations
SRC_DIR_REG=paceENSDF/TE/regular
SRC_DIR_TRANS=paceENSDF/TE/transient
TARG_DIR=paceENSDF

# Define internal installation option
OPT=0
while [ $# -gt 0 ]; do
    case $1 in
	-h | --help)
	    usage
	    exit 0
	    ;;
        -r | --regular)
	    cp -f $SRC_DIR_REG/ENSDF_JSON/*.json $TARG_DIR/ENSDF_JSON
	    cp -f $SRC_DIR_REG/PACE_JSON/*.json $TARG_DIR/PACE_JSON
	    OPT=1
	    echo "Copying decay data from $SRC_DIR_REG/ENSDF_JSON to $TARG_DIR/ENSDF_JSON"
	    echo "Copying coincidence data from $SRC_DIR_REG/PACE_JSON to $TARG_DIR/PACE_JSON"
	    ;;
	-t | --transient)
	    cp -f $SRC_DIR_TRANS/ENSDF_JSON/*.json $TARG_DIR/ENSDF_JSON
	    cp -f $SRC_DIR_TRANS/PACE_JSON/*.json $TARG_DIR/PACE_JSON
	    OPT=2
	    echo "Copying decay data from $SRC_DIR_TRANS/ENSDF_JSON to $TARG_DIR/ENSDF_JSON"
	    echo "Copying coincidence data from $SRC_DIR_TRANS/PACE_JSON to $TARG_DIR/PACE_JSON"
	    ;;
	*)
	    echo "Invalid option."
	    echo "Script usage: $(basename $0) [-r] [-t]" >&2
	    exit 1
	    ;;
    esac
    shift
done

if [ $OPT -eq 1 ];
then
    echo "ENSDF-decay datasets with regular intensities will be installed."
elif [ $OPT -eq 2 ];
then
    echo "ENSDF-decay datasets with transient equilibrium intensities will be installed."
else
    cp -f $SRC_DIR_REG/ENSDF_JSON/*.json $TARG_DIR/ENSDF_JSON
    cp -f $SRC_DIR_REG/PACE_JSON/*.json $TARG_DIR/PACE_JSON
    echo "Installation flag not specified:"
    echo "ENSDF-decay datasets with regular intensities will be installed."
fi

# Now onto cleaning up and building the project

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
