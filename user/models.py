import datetime

from django.db import models

from tools.model_to_dict import ModelMixin


class User(models.Model):
    SEX = (
        ('male','男'),
        ('female','女')
    )
    phonenum = models.CharField(max_length=20,unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=64,default='隔壁老王', verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birth_year = models.PositiveIntegerField(default=2000, verbose_name='出生年')
    birth_month = models.PositiveIntegerField(default=1, verbose_name='出生月')
    birth_day = models.PositiveIntegerField(default=1, verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=16,default='北京', verbose_name='常居地')

    class Meta:
        db_table = 'users'

    @property
    def age(self):
        today = datetime.date.today()
        birthday = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birthday).days // 365

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'age': self.age,
            'avatar': self.avatar,
            'location': self.location,
        }

    @property
    def profile(self):    # 获取个人资料
        if not hasattr(self, 'user_profile'):
            self.user_profile, _ = Profile.objects.get_or_create(id=self.id)  # 动态绑定属性
        return self.user_profile


class Profile(models.Model, ModelMixin):
    class Meta:
        db_table = 'profiles'

    SEX = (
        ('male', '男'),
        ('female', '女')
    )

    location = models.CharField(max_length=16, default='北京', verbose_name='目标城市')
    min_distance = models.PositiveIntegerField(default=0, verbose_name='最小查找范围')
    max_distance = models.PositiveIntegerField(default=50, verbose_name='最大查找范围')
    min_dating_age = models.PositiveIntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.PositiveIntegerField(default=50, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')
