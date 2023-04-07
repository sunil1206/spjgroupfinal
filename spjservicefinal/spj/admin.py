from django.contrib import admin
from .models import service, about, upcoming, slide, client, upcoming2, upcoming3, associate,gallery,gallery_foundation

# Register your models here.
admin.site.register(service)
admin.site.register(about)
admin.site.register(upcoming)
admin.site.register(upcoming2)
admin.site.register(upcoming3)
admin.site.register(slide)
admin.site.register(client)
admin.site.register(associate)
admin.site.register(gallery)
admin.site.register(gallery_foundation)