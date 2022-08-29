





Linux Driver for the Butterfly Media Compact Flash Adapter 




## Linux Driver for the Butterfly Media Compact Flash Adapter


### Introduction



The [Butterfly Media Compact Flash Adapter](http://www.butterflymedia.com/Products-CFReader.asp) is an inexpensive USB to
Compact Flash adapter which is based on the
[Prolific PL-2307B USB-ATAPI bridge controller](http://www.prolific.com.tw/pl2307.htm). To connect this
device to a Linux 2.4 system, I have adapted Enrico Bravin's usbide
BusLink 20 GB USB HD driver which is designed to interface with a similar
chip.

 Note: I've tried this out on a stock RedHat 7.2 kernel (2.4.7-10)
with good results, but a standard kernel 2.4.18 did \_not\_ work. There
have been some significant changes in the usb subsystem between 2.4.7
and 2.4.18, so Enrico's driver may need some updating.

### Installation



To begin, get Enrico's version 1.2.1 usbide driver at

[Enrico's Site](http://bravin.home.cern.ch/bravin/usbide/usbide.html)
uncompress/untar it and apply this patch

tar zxf usbide-1.2.1.tar.gz
  
gzip -cd butterfly\_patch-1.2.1.gz | patch -p0

Then, follow Enrico's excellent installation instructions to compile
and install the driver.

### Use



Once you've compiled and installed the driver, load the driver with some
variation of

modprobe usbide

and plug the adapter into the USB. Insert a CF card into the adapter.
Check the syslog and look for messages from the driver indicating
that it has detected the card. If all went well, you may create a
mount point for your card in the filesystem and mount the card. After
that, read and write the card as if it were an ordinary hard drive.
Before ejecting the card, unmount it.

### Automounting



On my stock Redhat 7.2 systems, I've set up the hotplug system to
automatically mount the compact flash card when the usb subsystem sees it.
Just grab my <usbide> script and put it in the /etc/hotplug/usb
directory. Then, add this line to /etc/fstab:

/dev/pda1 /mnt/cf auto noauto,owner 0 0

and create the mountpoint /mnt/cf. The next time you insert a Compact Flash
card it should be mounted and ready to use.

### Download


Get my patch here: <butterfly_patch-1.2.1.gz>
Please let me know if this patch works for you.


[Return to Linux page.](linux.html)
##### 
**Last Updated**


:2002-03-24
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)
  
 






















