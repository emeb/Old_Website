#!/bin/sh
# smallify all the images

for image in `cat images.txt`
do
	image_bare=${image%%.jpg}   # Strip off the old suffix
	new_suff=_sm.jpg           # new suffix
	image_new="$image_bare""$new_suff"
	echo $image " -> " $image_new
	convert $image -resize 640 $image_new
done

