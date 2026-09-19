from impacket.dcerpc.v5.dtypes import SID

print(SID(bytes.fromhex('0105000000000005150000005b7bb0f398aa2245ad4a1ca401020000')).formatCanonical())
