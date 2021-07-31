import json

def lambda_handler(event, context):
    
    username = '{fiap_user}'
    password = '{senha_123}'
    
    print("Usuário é {}".format(username))
    print("Senha é {}".format(password))
    
    return {
        'statusCode': 200
    }
