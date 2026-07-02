from django.shortcuts import render
from .models import Viagem, ProgramaFidelidade

def dashboard(request):
    viagens = Viagem.objects.all().order_by('-data_ida') # Pega as viagens da mais recente para a mais antiga
    programas = ProgramaFidelidade.objects.all()
    
    return render(request, 'dashboard.html', {
        'viagens': viagens,
        'programas': programas
    })