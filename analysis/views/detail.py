from django.views.generic import TemplateView
from use_case.calculation import Calculation

class DetailView(TemplateView):
    template_name = 'app/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = Calculation.get_hoge()
        print(context['message'])
        return context
