import json


with open(r"C:\Users\adils\OneDrive\Документы\GitHub\PP2\Lab4\JSON\template.json", 'r') as f:
    data = json.load(f)


header = "Interface Status\n" + "=" * 80 + "\n"
header += "{:<50} {:<20} {:<8} {}\n".format("DN", "Description", "Speed", "MTU")
header += ("-" * 50 + ' ' + "--------------------" + ' ' + '-' * 6 + ' ' + '-' * 6)

output = header
cnt = 0
for item in data['imdata']:
    dn = item['l1PhysIf']['attributes']['dn']
    description = item['l1PhysIf']['attributes'].get('descr', '')
    speed = item['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = item['l1PhysIf']['attributes'].get('mtu', '')

    output += "\n{:<50} {:<20} {:<8} {}".format(dn, description, speed, mtu)

print(output)
