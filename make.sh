#!/bin/bash

python3 ./calc_progress.py
python3 ./insert_text.py

echo "MAKING"
cd ../pokeemerald-master-translated/
make -j 8
echo "DONE"

cd ../pokeemerald-latin