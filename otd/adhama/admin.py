from django.contrib import admin
from .models import Job
from .models import Testimony

from .models import Blogs
from .models import LatestPosts

from .models import Training

# Register your models here.

admin.site.register(Job)

admin.site.register(Testimony)


admin.site.register(Blogs)

admin.site.register(LatestPosts)


admin.site.register(Training)
