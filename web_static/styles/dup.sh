#!/usr/bin/env bash
#This script duplicates the 2 to 3's
for _ in $(ls | cut -d "-" -f 2); do 
		cp "2-$_" "3-$_";
done;
