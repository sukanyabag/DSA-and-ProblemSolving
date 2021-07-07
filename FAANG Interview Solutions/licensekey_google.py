def licenseKeyFormatting(self, our_str: str, k: int) -> str:
        
        our_str = our_str.replace('-','').upper()[::-1]
        res = ''
        count = 0
        
        for license_key_elem in our_str:
            if count == k:
                res += '-'
                count = 0
            res += license_key_elem
            count += 1
            
        return res[::-1]
