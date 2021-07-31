import json
import os 

def lambda_handler(event, context):

    username = os.environ['username']
    password = os.environ['password']
    
    print("Usuário é {}".format(username))
    print("Senha é {}".format(password))
    
    return {
        'statusCode': 200
    }
