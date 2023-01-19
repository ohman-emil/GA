#!/bin/zsh

echo "Generating Difference Diagram..."

python3 src/diagrams/diff_inhomogeneous/diff_inhomogeneous.py 5
echo "System 5"

python3 src/diagrams/diff_inhomogeneous/diff_inhomogeneous.py 6
echo "System 6"

python3 src/diagrams/diff_inhomogeneous/diff_inhomogeneous.py 7
echo "System 7"

python3 src/diagrams/diff_inhomogeneous/diff_inhomogeneous.py 8
echo "System 8"