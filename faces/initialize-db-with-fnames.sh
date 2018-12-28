#!/bin/bash
set -x

while IFS= read -r file
do
sqlite3 ocean-metadata.db "insert into blobs (name) VALUES (\"$file\");" >> chomp
done < "all-ocean-fnames"
