import csv
import pyasn
import time
import datetime
import pickle
from math import *
from influxdb import client as influxdb
from influxdb import InfluxDBClient
from influxdb import SeriesHelper



db = influxdb.InfluxDBClient('127.0.0.1',8086,'reda','root','data')


class MySeriesHelper(SeriesHelper):
    """Instantiate SeriesHelper to write points to the backend."""

    # pylint: disable=too-few-public-methods

    class Meta:
        """Meta class stores time series helper configuration."""

        # The client should be an instance of InfluxDBClient.
        client = db

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'netflow'

        # Defines all the fields in this time series.
        fields = ['size']

        # Defines all the tags for the series.
        tags = ['ASNs','ASNd']

        # Defines the number of data points to store prior to writing
        # on the wire.
        bulk_size = 100000

        # autocommit must be set to True when using bulk_size

        autocommit = True



asndb = pyasn.pyasn('ipasn_20140513.dat')
data={}

def to_timestamp(datestring):
    return time.mktime(datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S").timetuple())

with open('august.week1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        i=1
        for row in reader:



            if i<10:
                i=i+1


            else:
                if ((i%100000)==0):
                    MySeriesHelper.commit()
                    print(i)

                if ((i%4)==0 and row[12]=='background'):


                    ASNs=asndb.lookup(row[2])[0]
                    ASNd=asndb.lookup(row[3])[0]
                    #ts=to_timestamp(row[0])
                    ts=row[0]
                    size=int(row[11])

                    MySeriesHelper(
                    time=ts,
                    ASNs=ASNs,
                    ASNd=ASNd,
                    size=size,
                     )



            i=i+1
