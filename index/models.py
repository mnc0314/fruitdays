from django.db import models


# Create your models here.
class User(models.Model):
    uphone = models.CharField(max_length=11, verbose_name='手机号')
    password = models.CharField(max_length=15, verbose_name='密码')
    uname = models.CharField(max_length=30, default='匿名', verbose_name='用户名')
    email = models.EmailField(null=True, verbose_name='邮箱')
    isAlive = models.BooleanField(default=True, verbose_name='用户状态')

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 商品类型
class GoodsType(models.Model):
    # 类别名称
    title = models.CharField(max_length=30, verbose_name='商品类别')
    # 类别描述
    description = models.TextField(null=True, verbose_name='类别描述')
    # 类别图片(数据库存图片只存名称),用到pillow处理图像
    picture = models.ImageField(upload_to='static/upload/goodsType', verbose_name='类别图片')  # 在项目目录下自动创建一个static文件夹

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name


# 商品信息
class Goods(models.Model):
    # 商品名称
    title = models.CharField(max_length=30, verbose_name='商品标题')
    # 商品价格(七位数，小数点后两位)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='商品价格')
    # 商品规格
    spec = models.CharField(max_length=30, verbose_name='商品规格')
    # 商品图片
    picture = models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片')

    # 增加对goostype的引用（一对多）
    goodsType = models.ForeignKey(GoodsType, null=True, verbose_name='商品类型', on_delete=models.CASCADE)

    # 商品状态
    isActive = models.BooleanField(default=True, verbose_name='销售中')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
