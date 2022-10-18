# GetFGPP
Get Fine Grained Password Policy

```
python3 fgpp.py -u Administrator -p Password -d n00py.local       
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
```

You must have have read access to the FGPP c=Container and FGPP Objects to enumerate this. By default, only admins have this right.
