from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='用户名称', help_text="名称")
    password = models.CharField(max_length=50, default='', verbose_name='密码', help_text="名称")
    salt = models.CharField(max_length=10, default='', verbose_name='盐值')
    type = models.IntegerField(default=0, verbose_name='类型', help_text="0:普通用户，1：管理员")
    create_time = models.BigIntegerField(default=0, verbose_name='创建时间')

    class Meta:
        ordering = ['id']
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name
    
class ArticleCategory(models.Model):
    name =  models.CharField(max_length=50, default='', verbose_name='文章分类名称', help_text="名称")
    parent_id =  models.IntegerField(default=0, verbose_name='上级id', help_text="0:普通用户，1：管理员")
    path = models.CharField(max_length=50, default='', verbose_name='分类路径', help_text="-0-")
    is_show = models.IntegerField(default=0, verbose_name='是否显示', help_text="0:显示，1：不显示")
    order = models.IntegerField(default=0, verbose_name='排序', help_text="越小级别越高")
    create_time = models.BigIntegerField(default=0, verbose_name='创建时间')
    update_time = models.BigIntegerField(default=0, verbose_name='修改时间')

    class Meta:
        ordering = ['id']
        verbose_name = '文章分类名称'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=150, verbose_name='文章标题')
    summary = models.TextField(max_length=230, verbose_name='文章摘要', default='文章摘要等同于网页description内容，请务必填写...')
    img = models.CharField(default='', max_length=150, verbose_name='文章图片')
    body = models.TextField(verbose_name='文章内容')
    create_time = models.BigIntegerField(default=0, verbose_name='创建时间')
    update_time = models.BigIntegerField(default=0, verbose_name='修改时间')
    views = models.IntegerField(verbose_name='阅览量', default=0)
    loves = models.IntegerField(verbose_name='喜爱量', default=0)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='文章分类')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除', help_text="0:没有，1：删除")
    is_public = models.IntegerField(default=0, verbose_name='是否私有', help_text="0:不是，1：是")
    is_verify = models.IntegerField(default=0, verbose_name='是否审核过', help_text="0:未审核，1：通过，-1：不通过")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    # def __str__(self):
    #     return self.title[:20]

class ArticleComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人')
    comment = models.TextField(max_length=230, verbose_name='评论内容')
    create_time = models.BigIntegerField(default=0, verbose_name='创建时间')
    update_time = models.BigIntegerField(default=0, verbose_name='修改时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title[:20]

