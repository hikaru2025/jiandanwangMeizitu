import re

contem=r'<li><a href="job.html"><span> *人才招聘</span></a></li>'
ll=re.findall(r'>\s*\*人才招聘\s*<',contem)
print(ll)