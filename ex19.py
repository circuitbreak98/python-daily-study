def passwd_to_dict1():
    dic = {}
    with open('/etc/passwd') as f:
        for line in f:
            a = line.split(":")
            #print(a)
            user, uid = a[0], a[2]
            dic[user] = int(uid)
    
    return dic

def passwd_to_dict():
    users = {}
    with open('/etc/passwd') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(":")
                users[user_info[0]] = int(user_info[2])
    return users


print(passwd_to_dict())