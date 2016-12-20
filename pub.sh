#!/bin/bash
set -x

mkdir tmp/src
mkdir tmp/ref

cd src
find . | grep '\.md' | sed 's/\.\///g' > ../sources.txt
# ls -w 1 src/*.md > sources.txt
# ls -w 1 src/ref/*.md >> sources.txt
cd ..

while IFS= read -r file
do
sed 's/img\//http\:\/\/blop.s3-us-west-2.amazonaws.com\/img\//g' src/$file | \
sed 's/doc\//http\:\/\/blop.s3-us-west-2.amazonaws.com\/doc\//g' > tmp/$file
done < "/home/ec2-user/cem/sources.txt"

rm /home/ec2-user/cem/sources.txt

cd tmp
mv ref/* .
ls -1 *.md | cut -f 1 -d '.' > sources.txt
while IFS= read -r file
do
docker run -v `pwd`:/source jagregory/pandoc -f markdown -t html-raw_html --standalone --css=solarized-dark.css $file.md > $file.html
sudo cp $file.html /var/www/html/
done < "/home/ec2-user/cem/tmp/sources.txt"

rm /home/ec2-user/cem/tmp/sources.txt

cd ../src
sudo cp emroseclub.php /var/www/html/
sudo cp empix.txt /var/www/html/
sudo cp link_list.txt /var/www/html/
sudo cp index.html /var/www/html/

cd ..
