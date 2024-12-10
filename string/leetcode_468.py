class Solution(object):
    def validIPAddress(self, queryIP):
        if '.' in queryIP:
            if self.valid_IPv4_address(queryIP):
                return "IPv4"
        elif ':' in queryIP:
            if self.valid_IPv6_address(queryIP):
                return "IPv6"
        return "Neither"

    @staticmethod
    def valid_IPv4_address(ip):
        octets = ip.split(".")
        if 4 != len(octets):
            return False
        for octet in octets:
            if len(octet) > 1 and octet[0] == '0':
                return False
            if not octet.isnumeric():
                return False
            if not 0 <= int(octet) <= 255:
                return False
        return True

    @staticmethod
    def valid_IPv6_address(ip):
        chunks = ip.split(":")
        if 8 != len(chunks):
            return False
        for chunk in chunks:
            if not 1 <= len(chunk) <= 4:
                return False
            for hex_chr in chunk:
                if hex_chr.isnumeric():
                    continue
                elif hex_chr.isupper():
                    if not 65 <= ord(hex_chr) <= 70:
                        return False
                elif hex_chr.islower():
                    if not 97 <= ord(hex_chr) <= 102:
                        return False
                else:
                    return False

        return True
