from django.contrib import admin
from polls_app.models import Polls, Profile


class PollsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Polls, PollsAdmin)


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)



