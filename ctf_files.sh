echo "These are all files for CTFs"

#Installing nmap
sudo apt install nmap

#Installing wordlists
mkdir /opt/wordlists
cd /opt/wordlists
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt

#Installing gobuster 
sudo apt install gobuster 

#installing dirbuster
sudo apt install dirbuster

#installing hydra
sudo apt install hydra

#installing john_the-Ripper
cd /opt 
git clone https://github.com/openwall/john -b bleeding-jumbo john
cd john/src/
./confiigure
make -s clean && make -sj4
cd ../run
./john --test 

#CLoning linPEAS
git clone https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS

#Cloning winPEAS
git clone https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS

#installing enum4linux
git clone https://github.com/CiscoCXSecurity/enum4linux.git

#Installing RustScan
wget https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb
dpkg -i rustscan_2.0.1_amd64.deb
rm -rfv rustscan_2.0.1_amd64.debe

