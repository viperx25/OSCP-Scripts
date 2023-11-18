#!/usr/bin/python3


# Initial OSCP scan
# 
# Pete Toth
# 17 NOV 2023

import os
import argparse
from colorama import Fore as fg
from colorama import Style as style


############
# SETTINGS #
############



WORDLIST_WEB_DIR = '/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt'
WORDLIST_WEB_FILES = '/usr/share/seclists/Discovery/Web-Content/common.txt'
WORDLIST_WEB_CGI = '/usr/share/seclists/Discovery/Web-Content/CGIs.txt'



#################
# Initial Setup #
#################


parser = argparse.ArgumentParser(description="Initial OSCP Scan")
parser.add_argument('target', type=str, help='IP address/hostname of the target box')

args = parser.parse_args()


def run(c):
    print(fg.GREEN + c)
    print(style.RESET_ALL)
    os.system(c)

def printc(s, l='*'):
    print(style.BRIGHT + fg.GREEN + f'[{l}] ' + style.RESET_ALL + s + '\n')



# create directory
printc("creating log directory")
run('mkdir logs')
printc("changing current directory to 'logs'")
os.chdir("logs")


# Start with NMap
cmd = f"nmap -sC -sV -vv -oN initial.nmap -p- {args.target}"
run(cmd)
cmd = f"nmap -sC -sU -vv -oN initial-udp.nmap {args.target}"
run(cmd)



######################
# DIGEST NMAP SCRIPT #
######################

port80 = False
port443 = False

with open('initial.nmap', 'r') as f:
    text = f.read()

with open('initial-udp.nmap', 'r') as f:
    text-udp = f.read()

port80 = True if '80/tcp' in text else False
port443 = True if '443/tcp' in text else False
portSMB = True if '139/tcp' in text or '445/tcp' in text else False
port389 = True if '389/tcp' in text else False
port2049 = True if '2049/tcp' in text else False

###################
# SMB Enumeration #
###################

if portSMB:
    printc('SMB detected!')

    cmd = f"smbclient -L -N //{args.target}/"
    run(cmd)

    cmd = f"smbmap -H {args.target}"
    run(cmd)



####################
# LDAP Enumeration #
####################

if port389:
    printc('LDAP detected')

    cmd = f"ldapsearch -x -H ldap://{args.target} -s base namingcontexts"
    run(cmd)


###################
# RPC Enumeration #
###################

if portSMB:
    
    cmd = f"rpcclient -U "" -N {args.target}"
    run(cmd)



###################
# NFS Enumeration #
###################

if port2049:
    print('detected NFS service')

    cmd = f"showmount -e {args.target}"
    run(cmd)






###################
# WEB ENUMERATION #
###################

if port80:
    cmd = f"gobuster dir -u http://{args.target}/ -w {WORDLIST_WEB_DIR} -s '200,204,403,500' -b '' -t 100 -e -x .php,.txt,.asp,.aspx -o gobuster_dir_initial.txt"
    run(cmd)
   
    printc("don't forget to check for vhosts!")

    cmd = f"nikto -h http://{args.target}/"
    run(cmd)

