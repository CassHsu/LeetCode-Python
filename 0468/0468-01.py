class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.vaildIPv4(IP):
            return "IPv4"
        if self.vaildIPv6(IP):
            return "IPv6"
        return "Neither"
        
    def vaildIPv4(self, ip):
        segs = ip.split('.')
        if len(segs) != 4:
            return False
        
        for s in segs:
            if not self.vaildIPv4Seg(s):
                return False
        return True
        
    def vaildIPv4Seg(self, seg):
        if len(seg) == 0:
            return False
        if len(seg) >= 2 and seg[0] == "0":
            return False
        
        try:
            n = int(seg)
            if n < 0 or n > 255:
                return False
        except:
            return False
        return True
        
    def vaildIPv6(self, ip):
        segs = ip.split(':')
        if len(segs) != 8:
            return False
        
        for s in segs:
            if not self.vaildIPv6Seg(s):
                return False
        return True
        
    def vaildIPv6Seg(self, seg):
        if len(seg) == 0 or len(seg) > 4:
            return False
        for s in seg:
            if s not in "0123456789abcdefABCDEF":
                return False
        return True
