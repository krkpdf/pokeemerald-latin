#!/bin/bash

MARKED=false

for arg in "$@"; do
    case "$arg" in
        --marked|--m)
            MARKED=true
            ;;
        *)
            echo "Unknown argument: $arg"
            echo "Usage: $0 [--marked|--m]"
            exit 1
            ;;
    esac
done

python3 ./calc_progress.py
python3 ./insert_text.py ./text/ ../pokeemerald-master-translated/ 

echo "MAKING UNMARKED"
cd ../pokeemerald-master-translated/ || exit 1
make -j 8
echo "DONE"

cd ../pokeemerald-latin || exit 1

if [ "$MARKED" = true ] && [ -d "./macronized/" ]; then
    echo "MAKING MARKED"
    python3 ./macronize.py || exit 1
    python3 ./insert_text.py ./macronized/ ../pokeemerald-master-translated-marked/ 

    cd ../pokeemerald-master-translated-marked/ || exit 1
    make -j 8
    echo "DONE"

    cd ../pokeemerald-latin || exit 1
fi