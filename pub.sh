#!/bin/bash
set -x

mkdir tmp/src
mkdir tmp/ref

# clear out the target where we'll assemble all the files
cd tmp
rm *
cd ..

# grab all the .md files somewhere off src
cd src
find . | grep '\.md' | sed 's/\.\///g' > ../sources.txt
cd ..

while IFS= read -r file
do
cat src/$file | python insertions-and-slideshows.py $file
done < "sources.txt"

rm sources.txt

cd tmp
# mv ref/* .  removed cuz the python app saves to tmp/ PERIOD
ls -1 *.md | cut -f 1 -d '.' > sources.txt
while IFS= read -r file
do
md2html $file.md -s solarized-dark.css > $file.html
sudo cp $file.html /var/www/html/
# cp $file.html ../html
done < "sources.txt"

# there are two different sources.txt files, one's in tmp/sources.txt, and they differ in content!

rm sources.txt

cd ../src/root-files
sudo cp -r * /var/www/html/
cd ..
