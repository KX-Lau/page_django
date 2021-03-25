"""
自定义分页组件
"""


class Pagination(object):

    def __init__(self, total_count, current_page, base_url, per_page=10, show_page=9):
        """

        :param total_count: 总数据量
        :param current_page: 当前页
        :param base_url: 要分页的url
        :param per_page: 每页显示的数据量
        :param show_page: 每页最多显示的页码数
        """

        self.total_count = total_count
        self.per_page = per_page
        self.show_page = show_page
        self.half_show_page = show_page // 2
        self.base_url = base_url

        total_page, more = divmod(total_count, per_page)
        self.total_page = total_page + 1 if more else total_page

        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1

        if current_page < 1:
            current_page = 1

        current_page = total_page if current_page > total_page else current_page
        self.current_page = current_page

    @property
    def start(self):
        """数据切片的起始"""
        return self.per_page * (self.current_page - 1)

    @property
    def end(self):
        """数据切片的终止"""
        return self.per_page * self.current_page

    def page_html(self):
        """返回页码html"""

        # 总数据量小于页面最多显示的页码数
        if self.total_count < self.show_page:
            show_page_start = 1
            show_page_end = self.total_page
        # 左边越界
        elif self.current_page - self.half_show_page < 1:
            show_page_start = 1
            show_page_end = self.show_page
        # 右边越界
        elif self.current_page + self.half_show_page > self.total_page:
            show_page_start = self.total_page - self.show_page + 1
            show_page_end = self.total_page
        else:
            show_page_start = self.current_page - self.half_show_page
            show_page_end = self.current_page + self.half_show_page

        page_list = []
        page_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
        # 首页
        page_list.append('<li><a href="{1}?page={0}">首页</a></li>'.format(1, self.base_url))
        # 上一页
        if self.current_page - 1 < 1:  # 没有上一页
            page_list.append(
                '<li class="disabled"><span aria-hidden="true">&laquo;</span></li>')
        else:
            page_list.append(
                '<li><a href="{1}?page={0}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.current_page - 1, self.base_url))

        for i in range(show_page_start, show_page_end + 1):
            if self.current_page == i:
                page_list.append('<li class="active"><a href="{1}?page={0}">{0}</a></li>'.format(i, self.base_url))
            else:
                page_list.append('<li><a href="{1}?page={0}">{0}</a></li>'.format(i, self.base_url))

        # 下一页
        if self.current_page + 1 > self.total_page:  # 没有下一页
            page_list.append(
                '<li class="disabled"><span aria-hidden="true">&raquo;</span></li>')
        else:
            page_list.append(
                '<li><a href="{1}?page={0}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.current_page + 1, self.base_url))
        # 尾页
        page_list.append('<li><a href="{1}?page={0}">尾页</a></li>'.format(self.total_page, self.base_url))

        page_list.append('</ul></nav>')

        # 页码html代码
        page_html = ''.join(page_list)

        return page_html
