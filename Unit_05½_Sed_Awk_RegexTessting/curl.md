    curl -s  http://woz.csmp.missouriwestern.edu/data/real/uszips.csv | awk -F, '/MO/ {print $4, $5, $1}' | sed s/\"//g | grep "Saint Joseph" > local.txt
