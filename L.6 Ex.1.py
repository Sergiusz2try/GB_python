from collections import Counter

with open('nginx_logs.txt', encoding='utf-8') as f:
    logs = []

    for row in f:
        remote_adr = row.split(' ')[0]
        type_and_res = row.split('"')[1]
        request_type = type_and_res.split(' ')[0]
        requested_resource = type_and_res.split(' ')[1]
        log = (remote_adr, request_type, requested_resource)
        logs.append(log)

    print(*logs, sep='\n')
