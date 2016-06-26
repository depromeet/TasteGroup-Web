
#from tastegroup import models as tastegroup_models
# Register your models here.

#admin.site.register(tastegroup_models.Contents)
#admin.site.register(tastegroup_models.User_x)

# Register your models here.
from django.contrib import admin
from tastegroup import models

admin.site.register(models.Region)
admin.site.register(models.Hashtag)
admin.site.register(models.Menu)
admin.site.register(models.Taste_user)
admin.site.register(models.Restaurant)
admin.site.register(models.Record)
admin.site.register(models.Satisfaction)
admin.site.register(models.Group)
admin.site.register(models.Image)
