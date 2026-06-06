import Zlib
string="hello world!helloworld!hello world!hello world!"
compressed=zlib.compressed(string.encode())
decompressed=zlib.decompress(string.decode())
print(f" compressed string is:{compressed}")
print(f"decompressed string is:{decompressed}")
