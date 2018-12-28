#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import boto3
import urllib
import urllib2
from PIL import Image
import requests
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
    cur.execute("SELECT name from blobs where NOT(scanned) ;")
    rows = cur.fetchall()
    for row in rows:
        faces = ""
        labels = ""
        blobname = "ocean-img.v3.tar/" + row[0]
        print row[0],
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
        updater = fmt.format(urllib.quote(str(labels)), urllib.quote(str(faces)), row[0])
        cur.execute(updater)
        print

        # don't do this stuff, just collect data with this code
#        url = 'http://p0p.s3-us-west-2.amazonaws.com/' + str(blobname)
        # print url
#        request = urllib2.Request(url)
#        img = urllib2.urlopen(request).read()
#        with open ('./tmp/' + row[0], 'w') as f: f.write(img)
#        im = Image.open('./tmp/' + row[0])

        # print im.size
#        box = (100, 100, 400, 400)
#        region = im.crop(box)
#        region.save("./chf3.jpg", "JPEG") # save a box of the image

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

#            pprint.pprint(faces[0])
