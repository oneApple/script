for i in $(lsof -i:1234|awk '{print $1}'|grep [^COMMAND]); 
do pkill $i; 
done
