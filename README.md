# GetFGPP
Get Fine Grained Password Policy

```
python3 fgpp.py -u Administrator -p Password -d n00py.local
Fine Grained Password policy objects found!

DN: CN=Password Settings Container,CN=System,DC=n00py,DC=local - STATUS: Read - READ TIME: 2022-10-22T22:52:23.635853

DN: CN=FGPP,CN=Password Settings Container,CN=System,DC=n00py,DC=local - STATUS: Read - READ TIME: 2022-10-22T22:52:23.635888

DN: CN=FGPP2,CN=Password Settings Container,CN=System,DC=n00py,DC=local - STATUS: Read - READ TIME: 2022-10-22T22:52:23.635954

Attempting to enumerate details...

Policy Name: FGPP
Description: Domain Users Policy
Lockout Threshold: 12
Policy Applies to: CN=Domain Users,CN=Users,DC=n00py,DC=local
Minimum Password Length: 7
Observation Window: 00:30:00
Lockout Duration: 00:30:00
Precedence: 1
Complexity Enabled: True
Reversible Encryption: False

Policy Name: FGPP2
Lockout Threshold: 0
Policy Applies to: CN=locked,OU=locked,OU=Employees,DC=n00py,DC=local
Minimum Password Length: 7
Observation Window: 00:30:00
Lockout Duration: 00:30:00
Precedence: 2
Complexity Enabled: True
Reversible Encryption: False

                                                                                                                                           python3 fgpp.py -u lowpriv -p Password -d n00py.local      
Fine Grained Password policy objects found!

DN: CN=Password Settings Container,CN=System,DC=n00py,DC=local - STATUS: Read - READ TIME: 2022-10-22T22:53:16.084483

DN: CN=FGPP,CN=Password Settings Container,CN=System,DC=n00py,DC=local - STATUS: Read - READ TIME: 2022-10-22T22:53:16.084521

DN: CN=FGPP2,CN=Password Settings Container,CN=System,DC=n00py,DC=local - STATUS: Read - READ TIME: 2022-10-22T22:53:16.084592

Attempting to enumerate details...

Could not enumerate details, you likely do not have the privileges to do so!

```

You must have have read access to the FGPP Container and FGPP Objects to enumerate this. By default, only admins have this right.
