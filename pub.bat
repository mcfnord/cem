dir /b src\*.md > sources.txt

for /F %%f in (sources.txt) DO copy /y src\%%f tmp\

cd tmp

for /F %%f in (..\sources.txt) DO pandoc --from=markdown --to=html --standalone --css=solarized-dark.css %%f > %%~nf.html

del *.md

for /f %%f in (..\sources.txt) DO call p %%~nf.html

del *.html

cd ..\src

call p emroseclub.php
call p empix.txt
call p link_list.txt

cd ..

del sources.txt
