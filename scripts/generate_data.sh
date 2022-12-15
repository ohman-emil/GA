#!/bin/zsh

echo "Generating Data..."

cd src

cd system1/data
python3 generate_data.py
cd ../..
echo "System 1 Done"

cd system2/data
python3 generate_data.py
cd ../..
echo "System 2 Done"

cd system3/data
python3 generate_data.py
cd ../..
echo "System 3 Done"

cd system4/data
python3 generate_data.py
cd ../..
echo "System 4 Done"

cd system5/homogeneous/data
python3 generate_data.py
cd ../../..
echo "System 5 Homogeneous Done"

cd system5/inhomogeneous/data
python3 generate_data.py
cd ../../..
echo "System 5 Inhomogeneous Done"

cd system6/homogeneous/data
python3 generate_data.py
cd ../../..
echo "System 6 Homogeneous Done"

cd system6/inhomogeneous/data
python3 generate_data.py
cd ../../..
echo "System 6 Inhomogeneous Done"

cd system7/homogeneous/data
python3 generate_data.py
cd ../../..
echo "System 7 Homogeneous Done"

cd system7/inhomogeneous/data
python3 generate_data.py
cd ../../..
echo "System 7 Inhomogeneous Done"

echo "All Systems Done"