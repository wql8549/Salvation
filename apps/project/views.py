from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, ListView
from django.core.paginator import Paginator

from project.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Project
    context_object_name = 'project'
    template_name = "project/project_list.html"
    search_value = ""
    order_field = "-updater"
    pagenum = 5  # 每页分页数据条数

    def get_queryset(self):
        search = self.request.GET.get("search")
        order_by = self.request.GET.get("orderby")

        if order_by:
            all_pro = Project.objects.all().order_by(order_by)
            self.order_field = order_by
        else:
            all_pro = Project.objects.all().order_by(self.order_field)

        if search:
            # 项目名称 、创建人、项目负责人、项目负责人姓名查询
            all_pro = all_pro.filter(
                Q(project_name__icontains=search) | Q(creator__icontains=search) | Q(
                    prjcet_personliable__project__project_name__icontains=search) | Q(
                    prjcet_personliable__username__icontains=search)
            )
            self.search_value = search

        self.count_total = all_pro.count()
        paginator = Paginator(all_pro, self.pagenum)
        page = self.request.GET.get('page')
        project = paginator.get_page(page)
        return project

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectListView, self).get_context_data(*args, **kwargs)
        context['count_total'] = self.count_total
        context['search'] = self.search_value
        context['orderby'] = self.order_field
        context['objects'] = self.get_queryset()
        return context
