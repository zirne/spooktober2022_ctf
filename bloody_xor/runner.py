def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text `text` as bytes and an encryption key `key` as a byte
    in range [0, 256) the function encrypts the text by performing
    XOR of all the bytes and the `key` and returns the resultant.
    """
    return bytes([b ^ key for b in text])


with open('chall.bin', mode="rb") as h:
    data = h.read()

search = bytearray('spooky', 'ascii')


for i in range(0, 256):
    r = single_byte_xor(data, i)
    if search in r:
        hex_codes = list(r)
        ret = []
        for x in hex_codes:
            try:
                c = chr(x)
                ret.append(c)
            except:
                pass
        stringdata = "".join(ret)
        halla = stringdata.split("spooky")
        print()