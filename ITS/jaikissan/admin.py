from django.contrib import admin


from .models import Kissan
from .models import Farm
from .models import Well
from .models import WellUpdate
from .models import FamilyMember
from .models import Question
from .models import Answer
from .models import Seed
from .models import Fertilizer
from .models import CropPrice
from .models import House

admin.site.register(Kissan)
admin.site.register(Farm)
admin.site.register(Well)
admin.site.register(WellUpdate)
admin.site.register(FamilyMember)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Seed)
admin.site.register(Fertilizer)
admin.site.register(CropPrice)
admin.site.register(House)
