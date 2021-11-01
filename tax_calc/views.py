from django.shortcuts import render

def tax_calc(request):
    return render(request, 'tax_calc.html', {})

