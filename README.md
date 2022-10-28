# Spooktober CTF #

## Intro ##

It's that time of the year again! Very little sleep, junk food and Powerking all around. I've been looking forward to 
this CTF since it was announced and even though there was a LOT of cursing (you made me install NodeJS, ugh) I'd do it 
all again. It felt like the challenges were quite a bit harder than last year, and still a lot of fun! Thanks to all 
involved in organizing this. <3

## About ##

Every Challenge has it's own directory with a readme in it. If you don't want to read the ramblings of a crazy person 
trying to remember how he hacked something three days ago, there's a TL:DR at the bottom. 

## Disclaimer ##

There's gonna be a lot of Python, some Node, a bunch of tools that works on Wintendo (It's neat when they do, and I 
don't use Arch btw). Buckle up. There might also be a bunch of curses in this repo since it contains notes made in a 
delirium at 3 AM after staring at Monster auction for five hours straight. I also might get some details wrong since I'm 
writing this on the Thursday and I don't really remember every little thing I did anymore. There's been a lot of Python 
code but I think most of it is here (both the experimental parts and the things that actually solved challenges).

## Preparation ##

New laptop with a fresh install of Windows 11 (The new terminal is the only good thing about this choice). WSL with 
Debian (a mistake, even though I love Debian), PyCharm (since working with Python becomes 10x easier that way), 
Docker Desktop, Burp Suite, Visual Studio and HxD Hex Editor. Some Warmup over at picoctf the day before and off to the 
races!

## General task rundown (In order of when I started to attack them) ##

I started with a quick look at the Web stuff, since that's my strength and the rest of my team had already done a bunch 
pwn plus the Web stuff from last year. Spent a couple of minutes on that while trying to find a good place to start, and 
eventually ended up working on [shred](./shred/README.md). After that, I heard complaints regarding 
[Behind Bars](./behind_bars/README.md), so I fixed that. That's about as far as I got that day since I spent the whole 
night staring at Monster Auction and Candy Vault.

The next day started with trying to get my mind off of Monster Auction (In retrospect, I knew the solution, just not the 
execution, which made me furious), so I decided to try my luck at understanding WARMUP: Lost his marbles and WARMUP: 
Return to Santa since I didn't solve them last year. Got them sorted out fairly quick (I don't bother doing writeups for
them since they already have excellent ones from last year). Still not wanting to look at the Web stuff I decided to do 
some forensics with [Movie Killer](./movie_killer/README.md) instead. 

After that it was time to sleep, and then 
overthink [Where's Jason](./wheres_jason/README.md). We don't speak of it no more. [Bloody XOR](./bloody_xor/README.md) 
up next (I did everything to avoid my Arch-Nemesis Monster Auction at this point), and trying to figure out what to XOR 
with was a fun activity for a bit. Eventually the rest of the team was looking at everything except Web things. So I had 
to start caring about PHP modules in [CandyVault](./candyvault/README.md) and that was probably my favorite of the bunch.

Pseudonym, on the other hand, was probably the most annoying challenge. After hours wasted I got it done and had only 
 Secure Token and Monster Auction left. Still avoiding the Auction, I took a swing at 
[Secure Token])(./secure_token/README.md), and got it done after the source code was released (much appreciated). At 
this point it was only the worst one left, but with new energy after solving token problems, I got cracking on 
[Monster Auction](./monster_auction/README.md) 
