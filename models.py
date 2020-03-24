from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import django.utils.timezone as timezone
# Create your models here.

#作为booktest的数据库连接源
class testdata(models.Model):
    book = models.CharField('书名',max_length=100)
    auth = models.CharField('作者',max_length=100)
    data = models.CharField('日期',max_length=100)


class members(models.Model):
    userid = models.IntegerField('工号', default=None)
    username = models.CharField('姓名', max_length=180, default=None)
    office = models.CharField('科室',default='尺寸工程',max_length=10)
    phone = models.IntegerField('手机号',default=None)
    Email = models.CharField('邮箱',max_length=100)
#     group_choices = (('DS','尺寸系统'), ('DV','尺寸认证'), ('ES','工程支持'))
#     group = MultiSelectField(u"股",choices=group_choices,null=True,blank=True)

class Onepage(models.Model):
    userid = models.IntegerField('工号',default=None)
    username = models.CharField('姓名',max_length=180,default=None)
    repdata = models.CharField(' 报告日期',max_length=180)
    issuedes = models.CharField('问题描述',max_length=180)
    carmodel = models.CharField('车型',max_length=180)
    issuesource = models.CharField('问题来源',max_length=180)
    specification = models.CharField('标准',max_length=180)
    actualstatus = models.CharField('实际数据',max_length=180)
    issueoccerstage = models.CharField('发生阶段',max_length=180)
    frequency = models.CharField('发生频次',max_length=180)

    #数据波动情况复选
    datastatus_choices = (('average  deviation', u'均值偏移'), ('status  variation', u'数据波动'))
    datastatus = MultiSelectField(u"数据显示", choices=datastatus_choices,null=True,blank=True)

    #图片上传
    issue_img = models.ImageField(upload_to='images',default="")  #指定文件存放的前缀路径，实际的路径就是 MEDIA_ROOT/logo/filename

    #富文本编辑内容数据
    issue_analysis = RichTextUploadingField(default='', verbose_name='问题分析')


class countersolution(models.Model):
    shortsolution = models.CharField('短期措施',max_length=200)
    longsolution = models.CharField('长期措施',max_length=200)

class dailyreg(models.Model):
    basement = models.CharField('基地',max_length=180,default=None)           #数据复选，算了太多了
    department = models.CharField('部门',max_length=180,default='VME')
    office = models.CharField('科室',max_length=180,default='DE')
    gro = models.CharField('股',max_length=180,default=None)
    position = models.CharField('岗位名称',max_length=180,default=None)
    #岗位等级复选
    level_type = (('Z', u'Z'), ('E', u'E'), ('G', u'G'), ('H', u'H'), ('I', u'I'))
    level = MultiSelectField(u"岗级", choices=level_type, null=True, blank=True)

    userid = models.CharField('工号',max_length=180,default=None)
    username = models.CharField('姓名',max_length=180,default=None)
    daytime = models.CharField('保存日期',max_length=180)
    # daytime = models.DateTimeField('保存日期',default = timezone.now)
    contactdetail = RichTextUploadingField(default='', verbose_name='接触记录')




