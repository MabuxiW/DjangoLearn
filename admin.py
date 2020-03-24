from django.contrib import admin
from mysite.models import testdata,Onepage,countersolution,members,dailyreg


#对图书后台进行设置
class UserAdmin(admin.ModelAdmin):
    #显示模型中数据条目的字段
    list_display = ('book','auth','data')
    #可以根据字段进行搜索查找
    search_fields = ('book','auth','data')
    # 可以根据字段进行筛选
    list_filter = ('book','auth','data')
    # 可以根据字段进行排序，前部加-则表示倒序
    ordering = ('data',)

    # 指定可以编辑的字段
    #list_editable = ['auth','data']
    # 指定可以编辑的字段2
    list_display_links = ('auth','book','data')

    # 指定每页显示的条数
    list_per_page = 5

    # 插入数据时，指定需要编辑的字段
    #fields = ('data',)
    # 插入数据时，指定不需要编辑的字段；这两个字段不可编辑
    #exclude = ('auth','book',)

admin.site.register(testdata,UserAdmin)



#对尺寸人员信息进行设置
class UserAdmin3(admin.ModelAdmin):
    #显示模型中数据条目的字段
    list_display = ('userid','username','office','phone','Email')
    # 指定可以编辑的字段2
    list_display_links = ('userid','username','office','phone','Email')

    # 指定每页显示的条数
    list_per_page = 5

admin.site.register(members,UserAdmin3)

#对一页纸问题数据进行设置
class UserAdmin2(admin.ModelAdmin):
    #显示模型中数据条目的字段
    list_display = ('userid','username','carmodel','issuedes','repdata')
    #可以根据字段进行搜索查找
    search_fields = ('userid','username','carmodel','issuedes','repdata')
    # 可以根据字段进行筛选
    list_filter = ('userid','username','carmodel','issuedes','repdata')
    # 可以根据字段进行排序，前部加-则表示倒序
    ordering = ('userid','username','carmodel','issuedes','repdata')

    # 指定可以编辑的字段
    #list_editable = ['auth','data']
    # 指定可以编辑的字段2
    list_display_links = ('userid','username','carmodel','issuedes','repdata')

    # 指定每页显示的条数
    list_per_page = 10

admin.site.register(Onepage,UserAdmin2)



#对一页纸报告长短期措施设置
class UserAdmin4(admin.ModelAdmin):
    #显示模型中数据条目的字段
    list_display = ('shortsolution','longsolution')

admin.site.register(countersolution,UserAdmin4)
#自定义admin网页头部信息 - 方法1  （暂不好使）
# class MyAdminSite(admin.AdminSite):
#     site_header = 'DE网络后台管理系统'    #此处显示页面标签
#     site_title = 'DE数据管理中心'    #此处显示头部标题
#
# admin_site = MyAdminSite(name="management")

# # admin_site = MyAdminSite(name="staff")

#对科室日接触记录设置
class UserAdmin5(admin.ModelAdmin):
    #显示模型中数据条目的字段

    list_display = ('basement', 'department', 'office', 'gro', 'position', 'level', 'userid', 'username', 'daytime', 'contactdetail')
    # 可以根据字段进行搜索查找
    search_fields = ('basement', 'department', 'office', 'gro', 'position', 'level', 'userid', 'username', 'daytime', 'contactdetail')
    # 可以根据字段进行筛选
    list_filter = ('basement', 'department', 'office', 'gro', 'position', 'level', 'userid', 'username', 'daytime', 'contactdetail')
    # 可以根据字段进行排序，前部加-则表示倒序
    ordering = ('basement', 'department', 'office', 'gro', 'position', 'level', 'userid', 'username', 'daytime', 'contactdetail')

    # 指定可以编辑的字段2
    list_display_links = ('basement', 'department', 'office', 'gro', 'position', 'level', 'userid', 'username', 'daytime', 'contactdetail')

    # 指定每页显示的条数
    list_per_page = 20
admin.site.register(dailyreg,UserAdmin5)



# 自定义admin网页头部信息 - 方法2：
admin.site.site_header = 'DE数据管理中心'
admin.site.site_title = 'DE网络后台管理系统'




