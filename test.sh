#!/bin/bash
#test bash script
if test $1 -gt 0
then
echo "$1 is positive"
fi

for((i=1;i<$1;i++))
do
echo "Welcome $1 * $i = `expr $i \* $1` times"
done
