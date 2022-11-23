#!/bin/sh


set -e

for kind in avg1 cube1 explode1 explode2 max1 rle1 sum1 uniq1 uniq2 uniq3 unmax1; do
    echo
    echo $kind
    echo '> go'
    :> /tmp/a
    go run $kind.go | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    echo '> js'
    node $kind.js| sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    echo '> py'
    python3 $kind.py| sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    echo '> c'
    gcc -Wall -Wextra -o /tmp/z $kind.c >/dev/null
    /tmp/z| sed -e 's/, /,/g'| sed -e 's/ /,/g' >> /tmp/a

    echo 'counted uniq:'
    cat /tmp/a | sort | uniq -c

    lines=$(cat /tmp/a | sort | uniq -c | wc -l)
    if [ "$lines" -ne "1" ]; then
        echo "NOOO"
        exit 1
    fi
done
                
