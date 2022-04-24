import string
import random

validString = string.ascii_letters + string.digits

class Codec:
    def __init__(self):
        self.m = {}
        
    def randstr(self):
        short = ""
        for _ in range(6):
            short += validString[random.randint(0, 10000) % 62]
            
        return short 
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.randstr()
        while key in self.m:
            key = self.randstr()
        
        self.m[key] = longUrl
        return "http://tinyurl.com/" + key
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.replace("http://tinyurl.com/", "")
        
        if shortUrl in self.m:
            return self.m[shortUrl]
        else:
            return None
