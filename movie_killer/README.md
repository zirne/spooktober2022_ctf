# Movie Killer #

## Process ##

Oh boy this was a pain in the butt. Since we were given just a zipfile with a user directory with just a bunch of files I started thinking 
about what I _couldn't_ use. No Event Log, no Global Registry. Starting from scratch, I started by looking at common 
browser artifacts. There were a couple of interesting folders (Chrome), but no profile data, just crashdump conf. I wrote 
some python scripts to remove empty files and empty directories in hopes of making the file list a bit easier to dig 
through but still couldn't find anything fun. 

I then decided to target the registry by loading the registry hive in 
Regedit and started to go through it by hand. Lots of Google searches like "Windows registry history" and 
"Windows appdata artifacts forensics" with a lot of variants on that theme. Trying different tools to look at the 
registry and files (I must have downloaded half of Nirsofts website), turns out looking for Search history and Web 
history history was a dead end. 

In my Google-spree, I saw a lot of talks about shellbags (which I knew about thanks to 
[this defcon talk](https://www.youtube.com/watch?v=NG9Cg_vBKOg)) and decided to try that route. I had an NTUSER.dat and 
a couple more files to take a swing at. I found [ShellBags Explorer](https://ericzimmerman.github.io/#!index.md) to open it 
with and... nothing in there. I searched for all .dat files and tried opeing those. 
"_%APPDATA%\Local\Microsoft\Windows\UsrClass.dat_" told me that there might be something interesting in 
"_%APPDATA%\Local\Microsoft\Terminal Server Client\Cache._" so I looked and there were files there! They must be 
important. I googled them and a [Youtube video](https://www.youtube.com/watch?v=NnEOk5-Dstw) titled 
"RDP Cache Forensics" came up.

Now, that might be data from when someone set up a VM for the challenge, but it's still worth looking at.
Turns out that static image data from RDP connections gets cached and stored in those files, and tools like 
[this](https://github.com/ANSSI-FR/bmc-tools) are able to extract that data. I got a bunch of small images, but I could 
distinguish a notepad window while scrolling through them. Paint to the rescue! Stitch the images together (Swearing 
isn't optional if you do this by hand, apparently there's tools for this but I didn't know at the time), get the flag.

## Toolkit ##

- [ShellBags Explorer](https://ericzimmerman.github.io/#!index.md)
- [bmc-tools](https://github.com/ANSSI-FR/bmc-tools)
- [Microsoft Paint](paint.exe)

## TL:DR ##
- Find RDP Cache files in "_%APPDATA%\Local\Microsoft\Terminal Server Client\Cache._"
- Extract Images using bmc-tools
- Stitch together with MS Paint (while swearing)
- Get flag
