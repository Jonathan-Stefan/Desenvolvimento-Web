from django.contrib import admin
from .models import Navigators, Mentorados, DisponibilidadeHorario, Reuniao


admin.site.register(Navigators)
admin.site.register(Mentorados)
admin.site.register(DisponibilidadeHorario)
admin.site.register(Reuniao)