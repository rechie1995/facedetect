#! /bin/sh

filenumber=0
for file in *.bmp
do 
	filename=${file%.bmp}
	filenumber=`expr $filenumber + 1`
	#mv $file ${filenumber}.bmp
	echo $file $filename $filenumber
done
