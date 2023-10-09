#!/usr/bin/env python3
from ldap3 import ALL, Server, Connection, NTLM, extend, SUBTREE
from dateutil.relativedelta import relativedelta as rd
import argparse
import time

parser = argparse.ArgumentParser(description='Dump Fine Grained Password Polices')
parser.add_argument('-u', '--username', help='username for LDAP', required=True)
parser.add_argument('-p', '--password', help='password for LDAP (or LM:NT hash)', required=True)
parser.add_argument('-l', '--ldapserver', help='LDAP server (or domain)', required=False)
parser.add_argument('-d', '--domain', help='Domain', required=True)

def base_creator(domain):
    search_base = ""
    base = domain.split(".")
    for b in base:
        search_base += "DC=" + b + ","
    return search_base[:-1]

def clock(nano):
    fmt = '{0.days} days {0.hours} hours {0.minutes} minutes {0.seconds} seconds'
    sec = int(abs(nano/10000000))
    return fmt.format(rd(seconds=sec))

def main():
    args = parser.parse_args()
    if args.ldapserver:
        s = Server(args.ldapserver, get_info=ALL)
    else:
        s = Server(args.domain, get_info=ALL)
    print("Attempting to connect...\n")
    c = Connection(s, user=args.domain + "\\" + args.username, password=args.password, authentication=NTLM,
                   auto_bind=True)
    print("Searching for Policy Objects...")
    c.search(search_base='CN=Password Settings Container,CN=System,'+ base_creator(args.domain), search_filter='(objectclass=*)')
    if len(c.entries) > 1:
            print(str(len(c.entries) - 1) + " FGPP Objects found! \n\nAttempting to Enumerate objects with an applied policy...\n")
            c.search(search_base=base_creator(args.domain), search_filter='(objectclass=*)',attributes=['DistinguishedName','msDS-PSOApplied'])
            for entry in c.entries:
                if str(entry['msDS-PSOApplied']) != "[]":
                        print ("Object: " + str(entry['DistinguishedName']))
                        print ("Applied Policy: " + str(entry['msDS-PSOApplied']))
                        print("")           
            print("Attempting to enumerate details...\n")
            c.search(search_base=base_creator(args.domain), search_filter='(objectclass=msDS-PasswordSettings)',
                     attributes=['name', 'msds-lockoutthreshold', 'msds-psoappliesto', 'msds-minimumpasswordlength',
                                 'msds-passwordhistorylength', 'msds-lockoutobservationwindow', 'msds-lockoutduration',
                                 'msds-passwordsettingsprecedence', 'msds-passwordcomplexityenabled', 'Description',
                                 'msds-passwordreversibleencryptionenabled','msds-minimumpasswordage','msds-maximumpasswordage'])
            if str(c.entries) != "[]":
                    for entry in c.entries:
                        print("Policy Name: " + str(entry['name']))
                        if str(entry['description']) != "[]":
                            print("Description: " + str(entry['description']))
                        print("Minimum Password Length: " + str(entry['msds-minimumpasswordlength']))
                        print("Minimum Password History Length: " + str(entry['msds-passwordhistorylength']))
                        print("Lockout Threshold: " + str(entry['msds-lockoutthreshold']))
                        print("Observation Window: " + clock(int(str(entry['msds-lockoutobservationwindow']))))
                        print("Lockout Duration: " + clock(int(str(entry['msds-lockoutduration']))))
                        print("Complexity Enabled: " + str(entry['msds-passwordcomplexityenabled']))
                        print("Minimum Password Age " + clock(int(str(entry['msds-minimumpasswordage']))))
                        print("Maximum Password Age: " + clock(int(str(entry['msds-maximumpasswordage']))))
                        print("Reversible Encryption: " + str(entry['msds-passwordreversibleencryptionenabled']))
                        print("Precedence: " + str(entry['msds-passwordsettingsprecedence']) + " (Lower is Higher Priority)")
                        for dn in entry['msds-psoappliesto']:
                            print("Policy Applies to: " + str(dn))
                        print("")
            else:
                    print("Could not enumerate details, you likely do not have the privileges to do so!")
    else:
        print("No Fine Grained Password Policies found!")
if __name__ == "__main__":
    main()
