How-to-run-the-program:

1) Convert SID to canonical form (Using ArgParse):
   $ python3 convertsid-clean.py 0105000000000005150000005b7bb0f398aa2245ad4a1ca451040000
   S-1-5-21-4088429403-1159899800-2753317549-1105

2) Convert SID to canonical form (HardCoded):
   $ python3 convertsid.py       
    S-1-5-21-4088429403-1159899800-2753317549-513

3) Convert Plain Text Password to NTLM for Silver Ticket (TGS) (Hardcoded)
   $ python3 convertplain2ntlm.py
   ef699384c3285c54128a3ee1ddb1a0cc
