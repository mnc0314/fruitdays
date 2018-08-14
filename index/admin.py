from django.contrib import admin
from .models import *


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    # 增加右侧过滤器
    list_filter = ['goodsType']
    # 增加顶层搜索字段
    search_fields = ['title']


class UserAdmin(admin.ModelAdmin):
    search_fields = ['uphone', 'uname', 'email']
    fieldsets = [
        ('基本设置', {
            'fields': ('uphone', 'password', 'uname', 'email'),
        }),
        ('高级设置', {
            'fields': ('isAlive',),
            'classes': ('collapse',),
        }),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(GoodsType)
admin.site.register(Goods, GoodsAdmin)
