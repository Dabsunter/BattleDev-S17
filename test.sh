#!/bin/bash

if [ $# -le 1 ]; then
    echo "bad usage: $0 <numéro de question>"
    exit 1
fi

nbtest=$2

for i in $(seq $nbtest); do
    echo "   ========== Test n°$i/$nbtest =========="
    cat exo$1/input$i.txt | time -p python3 exo$1.py 1> exo$1/myoutput$i.txt
    if diff -w exo$1/output$i.txt exo$1/myoutput$i.txt &> /dev/null; then
        echo "OK"
        echo
    else
        echo "KO"
        exit 1
    fi
done

echo "Success !"
