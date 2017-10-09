#!/bin/bash

while IFS= read -r file
do
echo -n aws rekognition detect-labels --image \'{\"S3Object\":{\"Bucket\":\"toop\",\"Name\":\"img/o/
echo -n $file
echo -n \"}}\'
echo \>\> $file.rek
done < "/home/ec2-user/all-ocean.txt"

