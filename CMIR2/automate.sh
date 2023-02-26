#! /bin/bash

for x in {500..700..20}
    do
    for y in {900..1100..20}
        do 
            python3 main.py $x $y
            # echo "$x $y"
    done
done

# for x in {19..1500..25}
#     do 
#         python3 main.py $x
#         # echo "scale=4;$x/10" | bc
# done