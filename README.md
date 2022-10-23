# GetFGPP

## Get Fine Grained Password Policy

Required: **pip3 install python-dateutil**

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
Policy Applies to: CN=Domain Users,CN=Users,DC=n00py,DC=local
Minimum Password Length: 6
Lockout Threshold: 100
Observation Window: 0 days 0 hours 30 minutes 0 seconds
Lockout Duration: 0 days 0 hours 30 minutes 0 seconds
Complexity Enabled: False
Minimum Password Age 1 days 0 hours 0 minutes 0 seconds
Maximum Password Age: 42 days 0 hours 0 minutes 0 seconds
Reversible Encryption: True
Precedence: 1

Policy Name: DA Policy
Description: This policy applied to Domain Admins
Policy Applies to: CN=Domain Admins,CN=Users,DC=n00py,DC=local
Minimum Password Length: 14
Lockout Threshold: 3
Observation Window: 0 days 0 hours 30 minutes 0 seconds
Lockout Duration: 10675199 days 2 hours 48 minutes 5 seconds
Complexity Enabled: True
Minimum Password Age 1 days 0 hours 0 minutes 0 seconds
Maximum Password Age: 42 days 0 hours 0 minutes 0 seconds
Reversible Encryption: False
Precedence: 2

                                                                                                                                                                                          
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
