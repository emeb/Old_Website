





DOS FAT tools for the MPuls3 Ampigo




## DOS FAT Tools for the MPuls3 Ampigo


### Introduction



In early 2002 I bought an [MPuls3 Ampigo](http://www.mpuls3.com/ampigo3.html)
MP3 player. this is a cute little device which plays MP3 files stored on Compact Flash
(CF) cards. The CF cards can be written using the included Parallel Port cable and the
Ampigo, or with any other type of CF adapter, such as a PCMCIA or USB adapter.

At the time, I bought a
[ButterFly Media USB adapter](http://www.butterflymedia.com/Products-CFReader.asp)
which worked with Win9x, but not Linux. I have patched an existing USB driver to recognize
this device - look [here](butterfly.html) for more info. Since then I've also
gotten an inexpensive [CF PCMCIA adapter](http://www.pqiusa.com/our_products.htm)
which also works well.

Unfortunately, although Linux can read and write the CF cards, the Ampigo only
recognizes MP3 files which are written by Win9x. The reason is simple - the DOS
FAT filesystem specifies that the EOC (end of cluster) marker is any value of
0xff8-0xfff for FAT12 or 0xfff8-0xffff for FAT16. Linux uses 0xff8 and 0xfff8
respectively, while Win9x uses 0xfff and 0xffff. The Ampigo only recognizes
0xfff and 0xffff!

To get around this, I've written a simple program which scans the FAT of an
unmounted DOS filesystem, correcting the EOC markers where necessary and writing
the results back to the filesystem.

### Compiling and Using



To begin, grab the code below.

uncompress/untar it, cd to the directory and compile

tar zxf fattools.tar.gz
  
cd fattools
  
make

Then, after writing some MP3 files to a CF card, sync and unmount it. When
the unmount process has complete, run 'winfat' on it:

./winfat device

 winfat will tell you what it has found and fixed. That's it! Pop the CF card
out and try it out in your Ampigo.

### Download


Get the code here: <fattools.tar.gz>
Please let me know if these tools for you.


[Return to Linux page.](linux.html)
##### 
**Last Updated**


:2002-02-04
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)
  
 






















