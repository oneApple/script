#!/bin/bash
date 
i=0 

while [ $i != "50" ] 

do 

i=`expr $i + 1` 
#或
#i=$(($i+1))
./client.py&

done 
date


