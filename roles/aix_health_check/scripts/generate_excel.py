# =====================================================
# roles/aix_health_check/scripts/generate_excel.py
# =====================================================
# Python dependency: openpyxl
from openpyxl import Workbook
import json, sys


data = json.loads(sys.argv[1])
outfile = sys.argv[2]


wb = Workbook()
ws = wb.active
ws.title = "AIX Health"


headers = [
'Host','IP','OS Level','Uptime','CPU Idle %','Mem Comp %',
'Paging','NTP','Cluster','IOCP','maxuproc','Disk','Errors'
]
ws.append(headers)


for h in data:
ws.append([
h['host'], h['ip'], h['oslevel'], h['uptime'],
h['cpu_idle'], h['mem_comp'], h['paging'], h['ntp'],
h['cluster'], h['iocp'], h['maxuproc'], h['disk'], h['errors']
])


wb.save(outfile)