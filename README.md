# Meraki Policy
Fetches Meraki MX Firewall, Parses for Match in L3 Policy


## Requirements or Prerequisites

Python v3 and a Meraki API key
Place the key inside the python files where noted.
See the following link for the control script - https://github.com/meraki/automation-scripts

## Usage

Once youve retrieved the Meraki Automation file, run it as
python MXfirewall.py -k <YOUR_API_KEY> -o /all -c create-backup", shell=True
Note the file it outputs as Meraki-Config<timestamp>.txt

then run the check script with an arguement to search for 8.8.8.8 in the MerakiConfig.txt
  
python3 MerakiCheckL3Rules.py --var1 8.8.8.8

A Sample L3 policy file is provided.
  
## Acknowledgements

Meraki Automation team for the MX Control Script.
https://github.com/meraki/automation-scripts

## Support

These are being shared freely without any stated or implied support and are for educational purposes only.  

If you'd like to contact me, please open an issue here and I'll reach out. 

Thanks.

T
