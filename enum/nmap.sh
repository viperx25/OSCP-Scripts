#!/bin/bash

read -p "enter ip: " ip

nmap -sC -sV -vv -oN initial.nmap $ip
nmap -sC -sV -vv -oN initial-ap.nmap -p- $ip
