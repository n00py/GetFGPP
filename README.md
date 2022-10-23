# GetFGPP
Get Fine Grained Password Policy

```
python3 fgpp.py -u Administrator -p Password -d n00py.local
Attmepting to connect...

Searching for Policy objects...
2 FGPP Objects found! 

Attempting to Enumerate objects with an applied policy...

Object: CN=Domain Admins,CN=Users,DC=n00py,DC=local
Applied Policy: CN=DA Policy,CN=Password Settings Container,CN=System,DC=n00py,DC=local

Object: CN=Domain Users,CN=Users,DC=n00py,DC=local
Applied Policy: CN=DU Policy,CN=Password Settings Container,CN=System,DC=n00py,DC=local

Attempting to enumerate details...

Policy Name: DU Policy
Description: This Policy Applies to Domain Users
Lockout Threshold: 100
Policy Applies to: CN=Domain Users,CN=Users,DC=n00py,DC=local
Minimum Password Length: 6
Observation Window: 00:30:00
Lockout Duration: 00:30:00
Precedence: 1
Complexity Enabled: False
Reversible Encryption: True

Policy Name: DA Policy
Description: This policy applied to Domain Admins
Lockout Threshold: 3
Policy Applies to: CN=Domain Admins,CN=Users,DC=n00py,DC=local
Minimum Password Length: 14
Observation Window: 00:30:00
Lockout Duration: 10:00:00
Precedence: 2
Complexity Enabled: True
Reversible Encryption: False

                                                                                                                                           python3 fgpp.py -u lowpriv -p Password -d n00py.local      
Attmepting to connect...

Searching for Policy objects...
2 FGPP Objects found! 

Attempting to Enumerate objects with an applied policy...

Object: CN=Domain Admins,CN=Users,DC=n00py,DC=local
Applied Policy: CN=DA Policy,CN=Password Settings Container,CN=System,DC=n00py,DC=local

Object: CN=Domain Users,CN=Users,DC=n00py,DC=local
Applied Policy: CN=DU Policy,CN=Password Settings Container,CN=System,DC=n00py,DC=local

Attempting to enumerate details...

Could not enumerate details, you likely do not have the privileges to do so!


```

You must have have read access to the FGPP Container and FGPP Objects to enumerate this. By default, only admins have this right.
