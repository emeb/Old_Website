





iodump




## 
I/O Space Dump utility


### What is it?


Have you ever wanted to look at your I/O space, but couldn't because
it's locked up by the kernel? Here's a little (I mean \_LITTLE\_)
kernel module that takes load time parameters and dumps I/O space to the
syslog so you can see what's where in a nice hexdump format. When it is
done, it exits without installing anything so you can run it again and
again. 

### Downloading


Get it here: <iodump-20001210.tar.gz>
### Compiling


After untarring, Simply type 'make' to compile the module.

### How to use it


Once you've compiled it, load it with the following command:

/sbin/insmod ./iodump.o addr\_start='start' addr\_len='bytes'

replacing 'start' and 'bytes' with the starting address in I/O space and
the number of bytes to dump. The two parameters should be in C hex format,
so an example might look like this:

/sbin/insmod ./iodump.o addr\_start=0x6100 addr\_len=0x80

which would dump the 128 bytes of I/O starting at location 6100 hex. The output
will appear in the syslog (/var/log/messages on my RH6.2 machine) and will be
formatted as follows:

> 
>   
> Oct 26 21:03:26 eisen kernel: iodump: version 0.01 time 12:11:32 Oct 26 2000 
>   
> Oct 26 21:03:26 eisen kernel: 6100: 00 ff 00 ff 00 ff 00 ff 
>   
> Oct 26 21:03:26 eisen kernel: 6108: 00 ff 00 ff 00 ff 00 ff 
>   
> Oct 26 21:03:26 eisen kernel: 6110: 00 ff 00 ff 00 ff 00 ff 
>   
> Oct 26 21:03:26 eisen kernel: 6118: 12 00 04 00 88 88 88 88 
>   
> Oct 26 21:03:26 eisen kernel: 6120: 00 ff 00 ff 00 ff 00 ff 
>   
> Oct 26 21:03:26 eisen kernel: 6128: 00 ff 00 ff 00 ff 00 ff 
>   
> Oct 26 21:03:26 eisen kernel: 6130: 00 00 00 00 00 00 00 30 
>   
> Oct 26 21:03:26 eisen kernel: 6138: 00 00 00 00 00 00 00 00 
>   
> Oct 26 21:03:26 eisen kernel: 6140: 01 0f 00 00 00 00 00 00 
>   
> Oct 26 21:03:26 eisen kernel: 6148: 00 00 ff ff 00 00 01 01 
>   
> Oct 26 21:03:26 eisen kernel: 6150: 00 00 00 00 00 00 00 00 
>   
> Oct 26 21:03:26 eisen kernel: 6158: 00 00 00 00 00 00 00 00 
>   
> Oct 26 21:03:26 eisen kernel: 6160: f7 f6 01 01 ff ff 01 01 
>   
> Oct 26 21:03:26 eisen kernel: 6168: 01 01 01 01 00 f6 00 f6 
>   
> Oct 26 21:03:26 eisen kernel: 6170: 00 01 00 01 00 01 00 01 
>   
> Oct 26 21:03:26 eisen kernel: 6178: 00 01 00 01 00 01 00 01 
>   
> Oct 26 21:03:26 eisen kernel: iodump: dump complete. 
> 


### Cautions


This is a development and debugging tool intended for use by people who
know what they're doing. Randomly reading I/O space can lock your machine
up solid if you're not careful (and sometimes even if you are!),
so sync your disks and expect the worst before running this tool.
Oh, and don't blame me if you lose something important anyway.

### Final remarks


This tool was written to support the development of the Maestro3/Allegro
sound driver. Thanks to Zach Brown for spearheading that project and for
putting up with my stupid questions as I learn about writing kernel code.

  

Linux - Yeah!

[Return to Linux page.](linux.html)
##### 
**Last Updated**


:12/10/00
##### 
**Comments to:**


[Eric Brombaugh](mailto:ebrombaugh1@cox.net)
  
 














