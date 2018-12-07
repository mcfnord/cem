#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import boto3
import urllib

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def main():
    database = "./ocean-metadata.db"

    client=boto3.client('rekognition')

    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name from blobs where NOT(scanned) LIMIT 2;")
        rows = cur.fetchall()
        for row in rows:
            blobname = "ocean-img.v3.tar/" + row[0]
            response = client.detect_labels(Image={'S3Object':{'Bucket':'p0p','Name':blobname}})
#            print response['Labels']
            updater = "UPDATE blobs SET scanned=1, labels='" + urllib.quote(str(response['Labels'])) + "' WHERE name = '" + row[0] + "';"
            cur.execute(updater)
#            print('Detected labels for ' + blobname)
#            for label in response['Labels']:
#                print (label['Name'] + ' : ' + str(label['Confidence']))

if __name__ == '__main__':
    main()
