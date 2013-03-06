#!/bin/bash
date 
i=0 

while [ $i != "100" ] 

do 

i=`expr $i + 1` 
#或
#i=$(($i+1))
./dev.py&

done 
date


