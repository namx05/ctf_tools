#Starts python server with default port i.e. 80
up $1(){
    python3 -m http.server $1
}

#Starts ftp server
upftp $1(){
	python3 ~/ctf/scripts/ftp.py $1
}

#Open butp-suite
burp(){
    cd /opt/burp-suite/; java -jar Loader.jar; cd - 
}

#connects to tryhackme VPN  
thmconnect(){
    sudo openvpn ~/thm/namx05.ovpn
}

#pepelope
listner $1(){
    cd /opt/penelope/; ./penelope.py $1; cd -
}

#python pty
pty(){
    cat /home/naman/ctf/scripts/ptyshell
}

#command cheatsheet
alies(){
    python3 /home/naman/ctf/scripts/alias.py
}

#tun0 ip
myip(){
    cat /home/naman/ctf/scripts/ip.sh | bash
}

#pwnkit remediation
pwnkit(){
    echo 'sudo chmod 0755 `which pkexec`'
}

#nmap
nmapscan(){
    sudo nmap -sS -sC -T4 -sV -Pn -p- -oN nmap $IP
}

#rustscan
rust(){
    sudo rustscan -a $IP --ulimit 2500 | tee rustscan.txt
}

#feroxbuster
feroscan(){
    feroxbuster -a $IP -o ferobuster.txt
}

#gobuster 
gobusterscan(){
    gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.txt -x php,html,txt
}

#ssti
ssti(){
    echo "ssti <url> <vuln_param> <command_to_execute>
    python /opt/ssti/tplmap -u $1 -d $2 --os-cmd "$3"
}

