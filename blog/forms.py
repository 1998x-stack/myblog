from django import forms
from captcha.fields import CaptchaField
from .models import Article


class CommentForm(forms.Form):
    visitor_name = forms.CharField(label='昵称', max_length=50)
    content = forms.CharField(label='评论内容', widget=forms.Textarea)
    captcha = CaptchaField(label='验证码')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['visitor_name'].required = False  # 设置 visitor_name 字段为可选
        self.fields['captcha'].required = False  # 设置 content 字段为可选
    
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']  # Add fields as necessary
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].required = False  # 设置 tags 字段为可选