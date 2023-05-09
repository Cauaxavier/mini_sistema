import urllib.request 

nome = str(input('Qual o nome do site(exemplo: pudim.com.br): '))
try:
    site = urllib.request.urlopen(f'http://www.{nome}/')
except urllib.request.URLError:
    print('Não foi possivel acessar o site.')
else:
    print('Conseguir acessar! O site está no ar') 

#código simples para descobrir se um site está acessivel ou não :3       
