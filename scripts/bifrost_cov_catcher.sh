#!/bin/bash

usage(){ 
    echo "Usage: ./bifrost_cov_catcher.sh number1 number2"  
} 

error(){ 
    echo "ERROR : invalid parameters !" >&2 
    usage 
    exit 1 
} 

# Parameter count
echo "Parameters : $#"
[[ $# -lt 2 ]] && error || usage

echo "-------------------------"
echo "Bifrost Cover Downloader"
echo "-------------------------"
echo "Prepare env..."

if [ -d "covers" ]
then
	rm -rf covers
fi
mkdir covers

echo "Retrieve covers..."

for number in $(seq $1 $2)
do
	echo "Page $number"
	url="https://www.belial.fr/revue/bifrost-$number"
	echo "Check URL exists:"
	exist=$(curl -Is $url | head -1 | cut -d' ' -f2)
	if [ $exist != "200" ]
	then
		echo "URL $url not available... Skipping cover number $number."
	else
	cover_url=$(curl -s $url |grep "Télécharger la couverture HD" | grep -o -E "[\"'](.*)[\"'] " | sed 's/"//g')
	echo "URL : $cover_url"
	echo "Downloading cover number $number..."
	echo "WGET : $cover_url"
	wget $cover_url -O covers/$number.jpg
	fi
	
done
