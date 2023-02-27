from django.contrib.auth.models import User
from app_news.models import NewsItem


def add_variable_to_context(request):
    users_unverified = User.objects.filter(groups__name='Зарегистрированные пользователи').count()
    unmoder_news = NewsItem.objects.filter(published=False).count()
    
    total_moders = users_unverified + unmoder_news
    
    return {
        'users_unverified': users_unverified,
        'unmoder_news': unmoder_news,
        'total_moders': total_moders,
    }
