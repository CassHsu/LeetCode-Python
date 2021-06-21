from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ret = defaultdict(int)
        
        for domains in cpdomains:
            count, domains = domains.split()
            count = int(count)
            
            domains = domains.split('.')
            for i in range(len(domains)):
                ret[".".join(domains[i:])] += count
        
        return ["{} {}".format(v, k) for k, v in ret.items()]
