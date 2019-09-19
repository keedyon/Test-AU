import hashlib

def encryption(Password_pass):
    md5 = hashlib.md5()
    md5.update(Password_pass)
    third_key = md5.hexdigest()
    return third_key

def default_key(base_password):
    default_salt = '($*ngr^@%'
    default_key = default_salt + base_password
    default_key_encoding = default_key.encode('utf-8')
    third_key = encryption(default_key_encoding)
    #md5= hashlib.md5()
    #md5.update(default_key_encoding)
    #third_key = md5.hexdigest()
    #print("---1----------")
    #print(third_key)
    return third_key

def get_second_key(checksum,base_password):
    checksum_four_key = checksum[0:4]
    first_four_key = checksum_four_key + default_key(base_password)
    first_four_key_encoding = first_four_key.encode('utf-8')
    second_key = encryption(first_four_key_encoding)
    #md5 = hashlib.md5()
    #md5.update(first_four_key_encoding)
    #second_key = md5.hexdigest()
    #print("--------2------------")
    #print(second_key)
    return second_key

def get_first_key(checksum,base_password):
    total_first_key = checksum + get_second_key(checksum,base_password)
    get_total_first_key = total_first_key.encode('utf-8')
    first_key = encryption(get_total_first_key)
    #md5 = hashlib.md5()
    #md5.update(get_total_first_key)
    #first_key = md5.hexdigest()
    #print("----------3--------------")
    #print(first_key)
    return first_key


q = get_first_key("98509b3af8b37ec206ae665eb807b764","111111")
print (q)

def version():
    return [
        {"version":"2.8.0"},
        {"version":"3.0.0"}
    ]

def get_account(num):
    accounts = []
    for index in range(1,num+1):
        accounts.append(
            {"account_name":"1880000019%s" % index,"original_password":'111111'},
        )

    return accounts






