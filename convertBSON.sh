#!/bin/bash

for i in *.bson; do
    [ -f "$i" ] || break
    bsondump $i --outFile=${i/\.bson/\.json}
done