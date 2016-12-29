#!/bin/bash
set -x

mkdir tmp/src
mkdir tmp/ref

cd src
find . | grep '\.md' | sed 's/\.\///g' > ../sources.txt
cd ..

while IFS= read -r file
do
sed 's/(img\//(http\:\/\/blop.s3-us-west-2.amazonaws.com\/img\//g' src/$file | \
sed 's/(doc\//(http\:\/\/blop.s3-us-west-2.amazonaws.com\/doc\//g' | \
        python add-insertions.py > tmp/$file
done < "sources.txt"

rm /home/ec2-user/cem/sources.txt

cd tmp
mv ref/* .
ls -1 *.md | cut -f 1 -d '.' > sources.txt
while IFS= read -r file
do
docker run -v `pwd`:/source jagregory/pandoc -f markdown -t html-raw_html --standalone --css=solarized-dark.css $file.md > $file.html
sudo cp $file.html /var/www/html/
done < "sources.txt"

# there are two different sources.txt files, one's in tmp/sources.txt, and they differ in content!

rm sources.txt

cd ../src
sudo cp emroseclub.php empix.txt link_list.txt index.html solarized-dark.css /var/www/html/
cd ..
