from django.shortcuts import render
from .models import Usuario, CalculoSolar

def calculo_solar(request):
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.POST.get('nome', '')
        ene_kwh = float(request.POST.get('ene_kwh').replace(',', '.'))
        ene_consumo = float(request.POST.get('ene_consumo').replace(',', '.'))
        hs = int(request.POST.get('hs', 0))
        dias = 30
        ano = 12

        # Etapa 1 - Calcular a potencia solar da região onde se encontra a casa.
        potencia = hs * dias
        sis_solar = potencia / ene_consumo

        # Etapa 2 - Calcular o valor de investimento para o seu sistema solar.
        soma = 300 + 4600 + 480 + 129 + 820 + 190 + 236 + 1000
        inv2 = sis_solar * soma
        inv3 = inv2 * hs

        # Etapa 3 - Calcular a produção mensal de energia.
        prod = sis_solar * hs * dias

        # Etapa 4 - Calcular economia anual do sistema solar.
        eco1 = sis_solar * potencia
        eco2 = eco1 * ano

        # Renderizar a página de resultado do cálculo
        return render(request, 'templates/resultado.html', {
            'nome': nome,
            'sis_solar': sis_solar,
            'inv3': inv3,
            'prod': prod,
            'eco2': eco2,
        })

    # Se o método da solicitação não for POST, renderize o formulário de cálculo
    return render(request, 'templates/formulario.html')