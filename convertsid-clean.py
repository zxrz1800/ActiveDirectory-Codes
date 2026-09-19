import argparse
from impacket.dcerpc.v5.dtypes import SID

parser = argparse.ArgumentParser(description="Convert a binary SID hex string to canonical format")
parser.add_argument("sid", help="SID as a hexadecimal string")
args = parser.parse_args()

print(SID(bytes.fromhex(args.sid)).formatCanonical())
