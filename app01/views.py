from django.shortcuts import render
from app01.models import User
from utils.mypage import Pagination


def user_list(request):
    query_set = User.objects.all()

    total_count = query_set.count()         # 总数据量
    current_page = request.GET.get('page', 1)   # 当前页
    base_url = request.path_info

    page_obj = Pagination(total_count, current_page, base_url)

    return render(request, 'user_list.html',
                  {'query_set': query_set[page_obj.start:page_obj.end], 'page_html': page_obj.page_html()})
