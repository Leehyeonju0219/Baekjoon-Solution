def solution(id_list, report, k):
    report_users = {}
    reported_users = {}
    for user_id in id_list:
        report_users[user_id] = []
        reported_users[user_id] = 0
    
    report = list(set(report))
    for rep in report:
        user_id, reported_id = rep.split()
        if reported_id in reported_users:
            reported_users[reported_id] += 1
        if user_id in report_users:
            report_users[user_id].append(reported_id)
    
    abandoned_id = {}
    for reported_user, cnt in reported_users.items():
        if cnt >= k:
            abandoned_id[reported_user] = True
    
    emails = {}
    for report_user, li in report_users.items():
        emails[report_user] = 0
        for reported_user in li:
            if reported_user in abandoned_id:
                emails[report_user] += 1
    
    return list(emails.values())