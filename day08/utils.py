import base64

def create_thunder_url(original_address):
    original_address = str(original_address)
    original_address = 'AA' + original_address + 'ZZ'
    print(original_address)

    original_address = original_address.encode('gbk')
    print(original_address)

    original_address = base64.b64encode(original_address)
    print(original_address)

    original_address = 'thunder://' + original_address.decode()
    thunder_address = original_address

    return thunder_address