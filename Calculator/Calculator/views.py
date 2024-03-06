from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,template_name='home.html')

n1 = 20
n2 = 10
def add(request):
    sum = n1 +n2
    return HttpResponse(f'<h1>Add Page<h1/> <br/> n1={n1}, n2={n2}, sum={sum}')

def sub(request):
    sub = n1 - n2
    return HttpResponse(f'<h1>Subraction Page<h1/> <br/> n1={n1}, n2={n2}, sub={sub}')

def mul(request):
    mul = n1 * n2
    return HttpResponse(f'Multiplication Page <br/> n1={n1}, n2={n2}, mul={mul}')


def mod(request):
    mod = n1 % n2
    return HttpResponse(f'Modulus Page <br/> n1={n1}, n2={n2}, mod={mod}')
