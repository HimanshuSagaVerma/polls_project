from django.contrib import admin
from polls_app.models import Polls


class PollsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Polls, PollsAdmin)



