# Monster Auction #

## Process ##

So.

Much.

Pain.

This hurt so badly. I had a theoretical exploit on friday, but I couldn't get it to work. Check out my 
[notes](./NOTES.txt) for madness in real-time (In Swedish, sorry). 

Anyway. We're tasked with finding the location of Jason. the javascript does a POST to the backend with body 
"name=whatever_we_put_in_the_search_field". It doesn't support any form of wildcard search, 
name=Ja doesn't return Jason or Jack the Ripper. Lousy search function. 
Can we search for other properties? let's try POSTing "location=Gotham", "location=Gotham City", "location=Batcave", 
"location=The Batcave", "location=Wayne Manor". Nothing. Well how about "location=Transylvania"? It returns "Dracula".

So we know that we can search for another property! That means that IF we're able to do partial matching, we could 
search letter by letter and figure out the location! I also discovered that POSTing "[name]=Jason" returns Jason! The 
express server probably does something funny!

During the upcoming days I stared at that search screen for HOURS. I installed NodeJS and got a 
[Hello World app](https://levelup.gitconnected.com/a-containerized-nodejs-express-hello-world-application-28d286556890) 
up and running so I could POST as much as I wanted and just console.log() my input to see what got out on the other 
side.

POSTing things like "name[key]=value" started creating very interesting objects inside the app.
```
{name: {key: "value"}}
```

So. I could create arbitrary objects on the server. Cool. Now what?

It was time to once again [RTFM](https://en.wikipedia.org/wiki/RTFM). 
I read up on Javascript Regex parsing, prototype pollution, JSON stringify XSS attacks but nothing seemed applicable to 
my situation. It was time to dig into the [Express Server Docs](https://expressjs.com/en/api.html).

The docs says that the default query parser is "extended", which means that it's using the 
[qs library](https://www.npmjs.com/package/qs).

Interesting, so the object behavior is a feature. Neat, still doesn't help me. More googling. "nodejs qs injection" 
seemed like a good place to start. I eventually stumbled upon a link (Currently missing, sorry) describing how quirky 
queries could open up for NoSQL Injections. Let's see how those work. There was a link to a page about NoSQL operators 
that unfortunately was dead, but wayback machine fixed that (Link currently missing, will add later).

In that list there was a glorious [regex operator](https://www.mongodb.com/docs/manual/reference/operator/query/regex/)

I could FINALLY run the attack I dreamt up a few days before. Wrote a python script that did it and got the last flag.

## Toolkit ##

- [NodeJS](https://nodejs.org/en/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

## TL:DR ##
- Discover "location" property by trying "location=Transylvania"
- Discover that you can build objects by writing funky parameters
- Create a NoSQL injection that allows you to regex match
- Try every character until you get a match, add that character to your search string until you have the complete flag