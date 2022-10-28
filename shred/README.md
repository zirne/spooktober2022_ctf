# shred #

## Process ##

My first challenge of the CTF! I spent more time on this than I probably should have. Opened the .img with a hex editor 
but at a first glance I saw nothing of value (didn't know the flag prefix at the time) so I tried a bunch of
tools to get it to either mount or list the files. Installed a Python Library (My favorite actitivity) to attempt to
extract files and got a vacation image plus a recipe for chicken pasta. Started digging for hidden data in EXIF headers,
looked at tools for hiding data in PDFs and digging through PDF properties, then looking at them with a Hex Editor but 
no luck. At this point I knew what the flag prefix was, and I started thinking about the fact that shred destroys 
EVERYTHING, not just individual files. Dug up [HxD](https://mh-nexus.de/en/hxd/) again, opened the .img, CTRL-F "spook",
Gottem.

## Toolkit ##

[HxD Hex Editor](https://mh-nexus.de/en/hxd/)

## TL:DR ##
- Open usb-backup.img in Hex Editor
- Press CTRL-F s p o o k y ENTER
- Get flag