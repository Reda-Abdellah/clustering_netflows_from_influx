clustering netflows from influx:
########################################

this repository contains a notebook and a script to insert data to influx db and than analyze its pattern using the notebook script

How to use:
=============

clone repository :

	clone git@github.com:Reda-Abdellah/clustering_netflows_from_influx.git

unzip the ipsan in the repository root folder:

	cd clustering_netflows_from_influx
	tar -xvzf ipasn_20140513.dat.tar.gz
 
install required packages:

	pip install csv pyasn time datatime pickle influxdb

you need to download dataset from https://nesg.ugr.es/nesg-ugr16/august.php
unzip it and run script to_influx.py
this script is for the first week , you will have to change the name of the file in line 63 so you can use it with the other weeks:
line 63: with open('august.week*.csv', newline='') as csvfile:
in our exemple we used all weeks of august

	jupyter-notebook 

and then choose ddos_detector.ipynb


