class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        m = {}
        
        for email in emails:
            local, domain = email.split("@")
            
            local = local.split("+")[0]
            local = "".join(local.split("."))
                    
            key = local + "@" + domain
            if key not in m:
                m[key] = 1
                
        return len(m.keys())
