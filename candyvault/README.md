# CandyVault #

## Process ##

I'm in a very complicated relationship with PHP, and it doesn't get any easier when you're involving C code. That's just 
mean. I spent quite some time staring at this and I couldn't have done it without a feroxbuster from Henok, revealing a 
bunch of files just lying around:

- http://spooktoberctf.se:22082/Dockerfile
- http://spooktoberctf.se:22082/docker-compose.yml
- http://spooktoberctf.se:22082/passwords.txt
- http://spooktoberctf.se:22082/public/bannedHashes.txt

That discovery was made before we finished _Where's Jason_, so I forgot about it for a while but I eventually scrolled 
back a bit and realized that the Dockerfile is very interesting, more so when the docker-compose.yml is there as well.

```
FROM php:7.4-apache
COPY . .
RUN cd extension && phpize && ./configure && make
RUN cp extension/modules/keyvault.so /var/www/keyvault.so
RUN cat passwords.txt | while read line; do echo -n "$line" | md5sum | cut -d" " -f1; done > public/bannedHashes.txt
RUN cp public/* /var/www/html/.
# Use the default production configuration
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
RUN echo "extension=/var/www/keyvault.so" >> "$PHP_INI_DIR/php.ini"
```
This gives me a couple of things:
- I can deploy this easily with Docker Desktop (as long as I have necessary files)
- It's running make. Is makefile available?
- If makefile is available, then could source be too?

```
erik@NONYABEESWAX:~$ curl --head http://spooktoberctf.se:22082/extension/Makefile
HTTP/1.1 200 OK
Date: Thu, 27 Oct 2022 14:09:59 GMT
Server: Apache/2.4.54 (Debian)
Last-Modified: Fri, 21 Oct 2022 13:46:29 GMT
ETag: "22d7-5eb8bab365740"
Accept-Ranges: bytes
Content-Length: 8919
```

Ooh, shiny! It mentions keyvault.c, and php_keyvault.h can i haz?

```
erik@NONYABEESWAX:~$ curl --head http://spooktoberctf.se:22082/extension/keyvault.c
HTTP/1.1 200 OK
Date: Thu, 27 Oct 2022 14:11:34 GMT
Server: Apache/2.4.54 (Debian)
Last-Modified: Fri, 21 Oct 2022 13:45:58 GMT
ETag: "7c8-5eb8ba95d5180"
Accept-Ranges: bytes
Content-Length: 1992
Content-Type: text/x-csrc
```

Got Headers?

```
erik@NONYABEESWAX:~$ curl --head http://spooktoberctf.se:22082/extension/php_keyvault.h
HTTP/1.1 200 OK
Date: Thu, 27 Oct 2022 14:13:02 GMT
Server: Apache/2.4.54 (Debian)
Last-Modified: Fri, 21 Oct 2022 13:45:58 GMT
ETag: "1ad-5eb8ba95d5180"
Accept-Ranges: bytes
Content-Length: 429
Content-Type: text/x-chdr
```

Yyyup. Now we're talking.

I had tried to get the module running in a VM, but apache's gonna apache and I didn't get it working in five minutes so 
I ditched that plan. I dediced to just deploy the docker container myself and add a docker volume so I could mess with 
the code from VScode. After reading up on some Zend Documentation to know which of the C-functions were exposed to PHP, 
I tested to write an index.php that looked like this:

```
<?php
$check = keyvault_check($_POST['password']);
if ($check == true){
    echo "Valid";
} else {
    echo "Invalid";
}
```

Now, I could try stuff!

Starting with 'asdf', and 'hunter2', I got 'Invalid' and 'Valid' respectively. That's not how the server treated me 
since the hash was banned. Could there be a md5-hashcheck in PHP before using the C-method?

```
<?php
$password = $_POST['password'];

$pw = array("hunter2", "hello_iver", "Sommar2020", "S3CuR3P4ssw000rd", "C4nDyISGREAT");
foreach($pw as $p){
    if (md5($p) == md5($password)){
        echo "Banned";
        die();
    }
}
$check = keyvault_check($_POST['password']);
if ($check == true){
    echo "Valid";
} else {
    echo "Invalid";
}
```

This behavior looked more like what's on the server.

After a bit of thinking, I realized that PHP and C _should_ mean that whatever input-string I fed to the server could be 
interpreted differently by the respective languages. Something that doesn't md5hash to the banned hashes but will be 
interpreted correctly by the C-program. C has Null-terminated strings, PHP doesn't do that.

Let's POST b'hunter2\x00'!

Winner winner, chicken dinner.

## Toolkit ##

[Docker Desktop](https://www.docker.com/products/docker-desktop/)
[VScode](https://code.visualstudio.com/)
[PyCharm](https://www.jetbrains.com/pycharm/)

## TL:DR ##
- Figure out that the check for banned hashes isn't a part of the PHP module (either by trial and error, or looking at source).
- Realize that PHP and C parses input differently.
- Bypass the check for banned hashes by appending a Null char to a known password
- Get flag