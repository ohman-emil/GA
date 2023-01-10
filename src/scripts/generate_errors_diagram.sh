#!/bin/zsh

echo "Generating Diagrams..."

python3 src/export_tikz_picture_errors.py 1
echo "System 1 Done"

python3 src/export_tikz_picture_errors.py 2
echo "System 2 Done"

python3 src/export_tikz_picture_errors.py 3
echo "System 3 Done"

python3 src/export_tikz_picture_errors.py 4
echo "System 4 Done"

python3 src/export_tikz_picture_errors.py 5_homogeneous
echo "System 5 Homogeneous Done"

python3 src/export_tikz_picture_errors.py 5_inhomogeneous
echo "System 5 Inhomogeneous Done"

python3 src/export_tikz_picture_errors.py 6_homogeneous
echo "System 6 Homogeneous Done"

python3 src/export_tikz_picture_errors.py 6_inhomogeneous
echo "System 6 Inhomogeneous Done"

python3 src/export_tikz_picture_errors.py 7_homogeneous
echo "System 7 Homogeneous Done"

python3 src/export_tikz_picture_errors.py 7_inhomogeneous
echo "System 7 Inhomogeneous Done"

python3 src/export_tikz_picture_errors.py 8_homogeneous
echo "System 8 Homogeneous Done"

python3 src/export_tikz_picture_errors.py 8_inhomogeneous
echo "System 8 Inhomogeneous Done"

echo "All Systems Done"