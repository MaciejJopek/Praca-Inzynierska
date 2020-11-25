import pyzipper

secret_password = b'lost art of keeping a secret'

# with pyzipper.AESZipFile('new_test.zip',
#                          'w',
#                          compression=pyzipper.ZIP_LZMA,
#                          encryption=pyzipper.WZ_AES) as zf:
#     zf.setpassword(secret_password)
#     zf.writestr('test.txt', "What ever you do, don't tell anyone!")

with pyzipper.AESZipFile('new_test.zip') as zf:
    zf.setpassword(secret_password)
    my_secrets = zf.read('test.txt')
    print (my_secrets)