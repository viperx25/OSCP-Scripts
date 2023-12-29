#!/bin/bash

read -p "enter base name (ex. backdoor.htb): " baseurl
echo "default wordlist: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt"
read -p "enter y if good, or enter the wordlist path: " good

if [ $good = "y" ]
then
	wordlist="/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt"
else
	wordlist=$good
fi

read -p "enter either http or https: " proto

wfuzz -w $wordlist -u "$proto://$baseurl" -H "Host: FUZZ.$baseurl" -t 50 --hc 302
