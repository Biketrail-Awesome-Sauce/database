from django.contrib import admin
from Data.models import MinnesotaBikeTrails
from Data.search_indexes import MinnesotaTrailsSearchable
# Register your models here.


admin.register((MinnesotaBikeTrails,MinnesotaTrailsSearchable))