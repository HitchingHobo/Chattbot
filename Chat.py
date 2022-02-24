from random import randint

print('Hej och välkommen till min chattbot, ska du inte hälsa?')

##Huvudloop för att kunna testa
while True:

    ##söker input efter hälsningsord
    def sök_hälsning(infras):
        hälsning_lista = [
            'Hej!', 
            'Tjena', 
            'Goddag', 
            'godkväll', 
            'hallå',
            'Näääämen haallååå elleer!',
            'Hejsan!'
        ]

        ##Väljer en random svarsfras på en hälsning
        if any(hälsning in infras for hälsning in hälsning_lista):
            index = randint(0,4)
            hälsning_svar_lista= [
                'Hej på dig',
                'Hallå eller',
                'I Grekland säger man typ yassou',
                'Trevlig att råkas',
                'Hej, visste du att min skapare heter Kostas?'
            ]
            return print(hälsning_svar_lista[index])
        else:
            return noll_svar()
     
    ## funktion för att returna ett slumpat 'noll'svar när vi inte känner igen något i inputen  
    def noll_svar():
        index = randint(0,4)
        noll_svar_lista = [
            'Sorry men jag zonade ut lite där', 
            'Har du sett Squidgames?', 
            'Jag vet inte vad du pratar om',
            'Asså jag har typ sett alla Marvelfilmer',
            'Jag glum...'
        ]
        return print(noll_svar_lista[index])       

    ##Formatering av input för att kunna söka lättare
    infras = input()
    infras = infras.lower()
    infras = infras.split()
    
    if 'slut' in infras:
        break
    
    sök_hälsning(infras)
    
    