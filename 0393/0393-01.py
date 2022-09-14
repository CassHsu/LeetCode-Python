class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        
        for n in data:
            bin_r = format(n, '#010b')[-8:]
            
            if n_bytes == 0:
                for bit in bin_r:
                    if bit == '0':
                        break
                    
                    n_bytes += 1
                    
                if n_bytes == 0:
                    continue
                    
                if n_bytes == 1 or n_bytes > 4:
                    return False
                
            else:
                if not (bin_r[0] == '1' and bin_r[1] == '0'):
                    return False
                
            n_bytes -= 1
            
        return n_bytes == 0
