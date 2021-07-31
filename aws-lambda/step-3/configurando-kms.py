import os
import boto3

from base64 import b64decode

USERNAME = os.environ['username']
PASSWORD = os.environ['password']

def lambda_handler(event, context):
    
    print('ENCRYPTED')
    
    print("Usuário é {}".format(USERNAME))
    print("Senha é {}".format(PASSWORD))

    print('DECRYPTED')
    
    print("Usuário é {}".format(decrypt_data(USERNAME)))
    print("Senha é {}".format(decrypt_data(PASSWORD)))

    return {
        'statusCode': 200
    }


def decrypt_data(ENCRYPTED):
    # Decrypt code should run once and variables stored outside of the function
    # handler so that these are decrypted once per container 
    return boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED), EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']})['Plaintext'].decode('utf-8')