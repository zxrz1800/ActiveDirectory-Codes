import sys
from impacket.dcerpc.v5.dtypes import SID

if len(sys.argv) != 2:
	print(f"Usage: {sys.argv[0]} <hex_sid>")
	sys.exit(1)

sid_hex = sys.argv[1]
print(SID(bytes.fromhex(sid_hex)).formatCanonical())
