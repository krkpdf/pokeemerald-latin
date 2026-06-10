#!/bin/bash

python3 ./calc_progress.py
python3 ./insert_text.py ./text/ ../pokeemerald-master-translated/ 

echo "MAKING UNMARKED"
cd ../pokeemerald-master-translated/
make -j 8
echo "DONE"

cd ../pokeemerald-latin

if [ -d "./macronized/" ]; then
    python3 ./insert_text.py ./macronized/ ../pokeemerald-master-translated-marked/ 

    echo "MAKING MARKED"
    cd ../pokeemerald-master-translated-marked/
    make -j 8
    echo "DONE"
fi


cd ../pokeemerald-latin