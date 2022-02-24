
infras=input('skriv något ')


def infras_vad():
    pass

def infras_hur():
    pass

def infras_varfor():
    pass

def noll_svar():
    pass


def main():
    while True:
        if infras == 'slut':
            break

        if 'vad' in infras:
            infras_vad()
        elif 'hur' in infras:
            infras_hur()
        elif 'varför' in infras:
            infras_varfor()
        else:
            noll_svar()






