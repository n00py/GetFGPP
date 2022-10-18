#!/usr/bin/env python3
from ldap3 import ALL, Server, Connection, NTLM, extend, SUBTREE
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
    seconds = abs(nano/10000000)
    ty_res = time.gmtime(seconds)
    res = time.strftime("%H:%M:%S",ty_res)
    return res

def main():
    args = parser.parse_args()
    if args.ldapserver:
        s = Server(args.ldapserver, get_info=ALL)
    else:
        s = Server(args.domain, get_info=ALL)
    c = Connection(s, user=args.domain + "\\" + args.username, password=args.password, authentication=NTLM,
                   auto_bind=True)
    try:
        c.search(search_base=base_creator(args.domain), search_filter='(objectclass=msDS-PasswordSettings)',
                 attributes=['name', 'msds-lockoutthreshold', 'msds-psoappliesto', 'msds-minimumpasswordlength',
                             'msds-passwordhistorylength', 'msds-lockoutobservationwindow', 'msds-lockoutduration',
                             'msds-passwordsettingsprecedence', 'msds-passwordcomplexityenabled',
                             'msds-passwordreversibleencryptionenabled', 'Description'])
        for entry in c.entries:
            print("Policy Name: " + str(entry['name']))
            if str(entry['description']) != "[]":
                print("Description: " + str(entry['description']))
            print("Policy Applies to: " + str(entry['msds-psoappliesto']))
            print("Minimum Password Length: " + str(entry['msds-minimumpasswordlength']))
            print("Observation Window: " + clock(int(str(entry['msds-lockoutobservationwindow']))))
            print("Lockout Duration: " + clock(int(str(entry['msds-lockoutduration']))))
            print("Lockout Threshold: " + str(entry['msds-lockoutthreshold']))
            print("Precedence: " + str(entry['msds-passwordsettingsprecedence']))
            print("Complexity Enabled: " + str(entry['msds-passwordcomplexityenabled']))
            print("Reversible Encryption: " + str(entry['msds-passwordreversibleencryptionenabled']))
            print("")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
