# Secure Token #

## Process ##

DISCLAIMER: I'm not sure I got all details 100% correct, so apologies in advance for any errors here.

JWTs are always fun! I hadn't played with JWKS before so this is probably what gave me the most new knowledge this CTF
(tyvm organizers <3).

I started reading up on common JWT attacks over at 
[hacktricks](https://book.hacktricks.xyz/pentesting-web/hacking-jwt-json-web-tokens)(great site). Downloaded 
[jwt_tool](https://github.com/ticarpi/jwt_tool/wiki), read the specs over at 
[RFC](https://www.rfc-editor.org/rfc/rfc7517) and more docs at 
[auth0](https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-key-sets) in the hope of finding something to take 
a swing at. At the same time starting to analyze the token payload. That jku property looked interesting, and I wondered 
if there might be a way to break the app by injecting something fun there (Spoiler alert, there was). I fired up a 
[Pipedream](https://pipedream.com) instance and created a bunch of JWTs with 
[PyJWT](https://pyjwt.readthedocs.io/en/latest/) but I couldn't get it to load my remote URL like that. I seemed to be 
locked to the local domain. I tried loading a JWKS from /token (and crashed the server, sorry about that) and eventually 
felt kinda stuck.

After a while the code for index.js was released. Now I could actually look at what was going on! I sat down and 
commented about every line to be able to follow what was happening. These lines in particular was interesting to me:
```
    try {
        var jwtPayload = parseJwt(req.body.jwt);
        if (!jwtPayload.jku) {
            return res.json("JKU claim is missing");
        }
        if (jwtPayload.jku.match(new RegExp(domain)) == null) {
            return res.json("That's not our JKU. Nice try script kiddie.");
        }
    } catch {
        return res.json("Invalid JWT token");
    }
```

That's just a regex match making sure the domain name (which is loaded from environment var, can't tamper that) is in 
the provided string. At this point I decided to test what would happen if I just added 'spooktoberctf.se' to my 
Pipedream URL. 

![Pipedream Request](get_req.png "Remote call!")

That's progress! Then we _should_ be able to create a JKWS, use that to sign our home-made tokens, and be on our way!

I had a lot of trouble creating both a JKWS that worked well. A couple of hours was spent with OpenSSL, jwt_tool and 
just TRYING to create both a JWKS and a good token but I kept getting an annoying message from the server:

"JWT signed with a token that's not ours. Nice try."

Shouting "HOW DO YOU KNOW THAT?!" in an apartment at 01:30 was a thing that happened.

Let's look at the code again:

```
    try {
        const keyStore = await nodeJose.JWK.asKeyStore(JSON.stringify(jwks));
        return nodeJose.JWS.createVerify(keyStore).
            verify(req.body.jwt).
            then(function(result) {
                if (jwtPayload.admin && jwtPayload.admin == true) {
                    return res.json({"admin": true, flag: process.env.FLAG});
                } else {
                    return res.json({"admin": false});
                }
            }).catch((err) => {
                return res.json("JWT signed with a token that's not ours. Nice try.");
            });
    } catch {
        return res.json("JWT verification failed unexpectedly.");
    }
```

jwks is what's specified in the provided token's jku, and we know that the jwks is fetched from our malicious jkws

At this point I decided to do the reasonable thing called [RTFM](https://en.wikipedia.org/wiki/RTFM), and looked at the
[library docs for node-jose](https://www.npmjs.com/package/node-jose#verifying-a-jws), specifically the part about 
verifying a jws. The documentation had a very interesting line:

```
NOTE: verify() will use the embedded key (if found and permitted) instead of any other key.
```

I also found [this interesting link](https://auth0.github.io/node-oauth2-jwt-bearer/interfaces/jwtheader.html#jku)

jku is a header property, but in the generated tokens from the site, it's a payload property. That's an implementation 
error! That should mean that specifying a jku in the header might be a part of the solution.

At this point, I've grown a bit frustrated with generating keys by hand and modifying tokens with jwt_tool. I was 
annoyed and lazy, soooo...


```
npm init -y
npm install express node-jose node-fetch --save
```

Why should I struggle with generating a keystore and creating tokens when that code is already written?
By modifying the code to present the private keystore on /jwks and create tokens where jku pointed to my malicious link
(both in the header and in the payload), and admin was true, I spun up the server, copied the JWKS, configured my 
pipedream endpoint to serve my JWKS as static content, generated a token, and got the frigging flag.


## Toolkit ##

[jwt_tool](https://github.com/ticarpi/jwt_tool/wiki)
[NodeJS](https://nodejs.org/en/)
[Pipedream](https://pipedream.com)

## TL:DR ##
- Read everything you can find about JWKS and JWTs.
- Realize that you can bypass domain lock by just appending the domain to wherever you want to host your own jwks
- Detect implementation error in token layout
- Create own JWKS and use it to create your own token with malicious header.jku, payload.jku and payload.admin = True.
- POST token.
- Get flag