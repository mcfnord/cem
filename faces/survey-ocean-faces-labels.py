#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import boto3
import urllib
import pprint
import json

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def main():
    database = "/home/ec2-user/cem/faces/ocean-metadata.db"

    client=boto3.client('rekognition')

    db = create_connection(database)
    cur = db.cursor()
    writecur = db.cursor()
    cur.execute("SELECT name from blobs where NOT(scanned) LIMIT 50 ;")
    rows = cur.fetchall()
    for row in rows:
        faces = ""
        labels = ""
        blobname = "ocean-img.v3.tar/" + row[0]
        print(row[0]),
        try:
            fullFacesResp = client.detect_faces(Image={'S3Object':{'Bucket':'p0p','Name':blobname}})
            faces = fullFacesResp['FaceDetails']
            # print faces
            # while these two lines work, i want a clean situation first
            #faces = responseFaces['FaceDetails']
            #print faces[0]['BoundingBox']
        except:
            print(" faces query failed."),

        try:
            fullLabelsResp = client.detect_labels(Image={'S3Object':{'Bucket':'p0p','Name':blobname}})
            labels = fullLabelsResp['Labels']
            # print labels
        except:
            print(" label query failed."),

        fmt = "update blobs set scanned=1, labels='{0}', faces='{1}' where name = '{2}';"
        updatestr = fmt.format(urllib.parse.quote(str(labels)), urllib.parse.quote(str(faces)), row[0])
        print (updatestr)
        writecur.execute(updatestr)
        print
    db.commit()
    db.close()

if __name__ == '__main__':
    main()

#            pprint.pprint(faces[0])
