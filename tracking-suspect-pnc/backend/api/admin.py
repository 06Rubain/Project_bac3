from django.contrib import admin
from .models import Commissariat, AgentPNC, Suspect, Photo

# Enregistrer chaque modèle pour qu'il soit visible dans l'interface admin
admin.site.register(Commissariat)
admin.site.register(AgentPNC)
admin.site.register(Suspect)
admin.site.register(Photo)