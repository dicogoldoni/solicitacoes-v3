import redis
import json
from time import sleep
from random import randint



if __name__=='__main__':
    r = redis.Redis(host='fila', port=6379, db=0)
    while True:
        mensagem = json.loads(r.blpop('envia')[1])
        print('Enviando a mensagem: ', mensagem['nome'])
        sleep(randint(10, 20))
        print('Mensagem', mensagem['nome'], 'enviada')