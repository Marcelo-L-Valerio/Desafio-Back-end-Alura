
from types import NoneType

def descricao_valida(descricao):
    return len(descricao) > 0

def descricao_unica_valida(data, model):
    all_releases = model.objects.all()
    aux = []

    if len(model.objects.filter(descricao = data['descricao']))>=1:
        for i in range(len(all_releases)):
            aux.append(all_releases[i].ano)

        if data['dia'].strftime('%Y') in aux:
            for j in range(len(all_releases)):
                
                if all_releases[j].mes == data['dia'].strftime('%m'):
                    return False

    return True

def valor_valido(valor):
    return valor > 0

def valor_numerico(valor):
    return type(valor) == int

def dia_valido(dia):
    return type(dia) != NoneType
