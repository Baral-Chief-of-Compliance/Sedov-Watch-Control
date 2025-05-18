from django.contrib import admin

from watch_control_app import models


@admin.register(models.crew_member.CrewMemeber)
class CrewMemeberAdmin(admin.ModelAdmin):
    list_display = ('cm_name', 'cm_surname', 'cm_patronymic', 'cm_status')
    search_fields = ('cm_name', 'cm_surname', 'cm_patronymic')
    save_on_top = True
    save_as = True


@admin.register(models.day_of_watch.DayWatch)
class DayWatchAdmin(admin.ModelAdmin):
    list_display = ('dw_date', 'dw_crew_member')
    search_fields = ('dw_date', 'dw_crew_member')
    save_on_top = True
    save_as = True


@admin.register(models.deck_place.DeckPlace)
class DeckPlaceAdmin(admin.ModelAdmin):
    list_display = ('dp_name',)
    search_fields = ('dp_name',)
    save_on_top = True
    save_as = True


@admin.register(models.deck.Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('d_name',)
    search_fields = ('d_name',)
    save_on_top = True
    save_as = True


@admin.register(models.institution.Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('i_name',)
    search_fields = ('i_name',)
    save_on_top = True
    save_as = True


@admin.register(models.post.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('p_name',)
    search_fields = ('p_name',)
    save_on_top = True
    save_as = True


@admin.register(models.role.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('r_name',)
    search_fields = ('r_name',)
    save_on_top = True
    save_as = True


@admin.register(models.watch.Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('w_start_date','w_end_date',)
    search_fields = ('w_start_date','w_end_date',)
    save_on_top = True
    save_as = True

@admin.register(models.work_time_interval.WorkTimeInterval)
class WorkTimeInterval(admin.ModelAdmin):
    list_display = ('wti_name',)
    search_fields = ('wti_name',)
    save_on_top = True
    save_as = True


@admin.register(models.work_time_period.WorkTimePeriod)
class WorkTimePeriodAdmin(admin.ModelAdmin):
    list_display = ('wtp_name','wtp_start_time', 'wtp_end_time',)
    search_fields = ('wtp_name','wtp_start_time', 'wtp_end_time',)
    save_on_top = True
    save_as = True