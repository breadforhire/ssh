#!/bin/bash

is_alive_ping()
{
  ping -c 1 $1 > /dev/null
  [ $? -eq 0 ] && echo $1 
}

for i in 10.0.0.{1..255} 
do
is_alive_ping $i 
done




