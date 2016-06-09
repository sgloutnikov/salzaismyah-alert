# Salza i Smyah Alert

Several popular plays at the Salza i Smyan Theater in Sofia sell out very quick after they are announced. Here is a script that can be run periodically to check the website for plays you care about and alert via email if they are available so you can go and buy your tickets on time :)

###Requirements 
* Python 3.51+
* Beautiful Soup 4.4.1+

###Usage
* Configure essentials (watch list, calendar url, SMTP) at top of script.
* Schedule to run script periodically. I use it with a cron job and run it every 12h. 

