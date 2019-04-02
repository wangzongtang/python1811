from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'     # form 取字段的时候,是按顺序取得

    def clean_max_distance(self):    # 固定写法,clean_+ 字段名
        clean_data = super().clean()   # 进行字段验证,会一个接一个验证,注意后字段获取出来,是不能与前字段比较的
        min_distance = clean_data['min_distance']
        max_distance = clean_data['max_distance']
        if min_distance > max_distance:
            raise forms.ValidationError('最小距离不能大于最大距离')

        return max_distance

    def clean_max_dating_age(self):
        clean_data = super().clean()
        min_dating_age = clean_data['min_dating_age']
        max_dating_age = clean_data['max_dating_age']
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('最小年龄不能大于最大年龄')

        return max_dating_age
