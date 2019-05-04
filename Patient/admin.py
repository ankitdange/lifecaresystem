from django.contrib import admin
from Patient.models import Patient_profile,Patient_appointment,Prescribed_medicine,Sale
admin.site.register(Patient_profile)
admin.site.register(Patient_appointment)
admin.site.register(Prescribed_medicine)
admin.site.register(Sale)

