from django.contrib import admin
from Data.models import MinnesotaBikeTrails
from Data.searchIndex import MinnesotaTrailsSearchable
# Register your models here.


admin.register((MinnesotaBikeTrails,MinnesotaTrailsSearchable))