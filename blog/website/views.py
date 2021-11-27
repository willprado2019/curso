from django.shortcuts import render



# def hello_blog(request):
#     return render(request, 'index.html')

def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'HTML',
        'Banco De Dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]

    data = {'name': 'Curso de Django 3',
    'lista_tecnologias': lista
    }
    return render(request, 'index.html', data)

