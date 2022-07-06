from cryptography.fernet import Fernet
#Steps
'''
1 - encode the message
2 - initialize the Fernet class
3 - pass the encoded message to encrypt() method
'''

# generate and save key
def gen_key():
    #    Gens key and saves to non py file
   
    try:
        key = Fernet.generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
        return 'success'.upper()
    except Exception as e:
        return ('fail'.upper())

def load_key():
    # get key
    return open('secret.key', 'rb').read()

def encrypt_data(data):
    key = load_key()
    encoded_data = data.encode()

    f = Fernet(key)
    encrypted_data = f.encrypt(encoded_data)
    return encrypted_data

def decrypt_data(encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    return(decrypted_data.decode(), '<-')

if __name__ == '__main__':
    runs = ['yes', 'yes'.capitalize(), 'y', 'yes'.upper()]
    ans = input('Gen key? ')
    
    if ans in runs:
        print(gen_key())
        x = encrypt_data('My name is Ashish')
        print(decrypt_data(x))
    