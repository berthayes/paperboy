#!/bin/sh
# A wrapper script to run ebook-convert from Calibre
# https://manual.calibre-ebook.com/generated/en/ebook-convert.html
# and call a python script to upload the results to myremarkable.com

# where downloaded newspapers.pdf get written
newspaper_dir="~/newspapers"

# File which is a list of Calibre news recipes
newspapers="dailies.txt"

datestamp=$(/bin/date +%Y-%m-%d)

cat $newspapers | while read line
do
  filepath=$(echo $line | tr [:space:] '_')
  filepath="$newspaper_dir/$filepath$datestamp.pdf"
  /Applications/calibre.app/Contents/MacOS/ebook-convert "$line.recipe" $filepath
  /usr/bin/python3 file2myrm.py $filepath
done
