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
    database = "/home/ec2-user/cem/rek/ocean-metadata.db"

    client=boto3.client('rekognition')

    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name from blobs where NOT(scanned) LIMIT 2;")
        rows = cur.fetchall()
        for row in rows:
            faces = None
            labels = None
            blobname = "ocean-img.v3.tar/" + row[0]
            try:
                responseFaces = client.detect_faces(Image={'S3Object':{'Bucket':'p0p','Name':blobname}})
                faces = responseFaces['FaceDetails']
            except:
                print("bad image format? some bad thing happened.")

            try:
                responseLabels = client.detect_labels(Image={'S3Object':{'Bucket':'p0p','Name':blobname}})
                labels = responseLabels['Labels']
            except:
                print("bad image format? some bad thing happened.")

            if labels is None:
                labels = ""
            if faces is None:
                faces = ""

            fmt = "update blobs set scanned=1, labels='{0}', faces='{1}' where name = '{2}';"
            updater = fmt.format(urllib.quote(str(labels)), urllib.quote(str(faces)), row[0])
            cur.execute(updater)
            print row[0]

#            if labels is not None:
#                updater = "UPDATE blobs SET scanned=1, labels='" + urllib.quote(str(response['Labels'])) + "' WHERE name = '" + row[0] + "';"
#            else:
#                updater = "UPDATE blobs SET scanned=1 WHERE name = '" + row[0] + "';"
#            cur.execute(updater)
#            print('Detected labels for ' + blobname)
#            for label in response['Labels']:
#                print (label['Name'] + ' : ' + str(label['Confidence']))

if __name__ == '__main__':
    main()
