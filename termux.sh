g='\033[1;32m'
p='\033[1;35m'
clear
echo -e "\033[1;32m"
clear
echo -e $g 'Please Wait ===+['$p'>              '$g']\'
sleep 0.2
cd main
nano users.txt 
clear
echo -e $g 'Please Wait ===+['$p'-------------> '$g']\'
sleep 0.2
pip3 install requests
clear
echo -e $g 'Please Wait ===+['$p'-------------->'$g']|'
sleep 0.2
pip3 install mechanize
python3 -m pip install requests
clear 
echo -e "$g+++++++++++++++>$p[Please Wait]$g<++++++++++++++"
sleep 0.4
chmod +x report.py
clear
echo -e "$g+++++++++++>[$p Welcome to the new update$p$g]<+++++++++++++"
sleep 1
python report.py

