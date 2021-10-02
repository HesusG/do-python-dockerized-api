from ipaddress import IPv4Network

class CidrMaskConvert():
    def cidr_to_mask(self, val):
        if val is None:
            return 'invalid'

        mask = '.'.join([str((0xffffffff << (32 - val) >> i) & 0xff) for i in [24, 16, 8, 0]])
        if mask == '0.0.0.0':
            return 'invalid'

        return mask

    def mask_to_cidr(self, val):
        if val is None:
            return 'invalid'

        cidr = sum([str(bin(int(octet))).count("1") for octet in val.split(".")])
        if cidr == 0:
            return 'invalid'

        return cidr

class IpValidate():
    def ipv4_validation(self, val):
        return True
