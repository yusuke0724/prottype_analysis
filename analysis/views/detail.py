from django.views.generic import TemplateView
from django.http import HttpResponse
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from use_case.calculation import Calculation
class DetailView(TemplateView):
    template_name = 'analysis/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = Calculation.get_hoge()
        print(self.cal())
        return context

    def cal(self):
        df = pandas.read_csv('data.csv')
        print(df)

        x = df[['x']]
        y = df[['y']]

        plt.plot(x, y, 'o')
        plt.show()

        model_lr = LinearRegression()
        model_lr.fit(x, y)

        plt.plot(x, y, 'o')
        plt.plot(x, model_lr.predict(x), linestyle="solid")
        plt.show()

        print('モデル関数の回帰変数 w1: %.3f' %model_lr.coef_)
        print('モデル関数の切片 w2: %.3f' %model_lr.intercept_)
        print('y= %.3fx + %.3f' % (model_lr.coef_ , model_lr.intercept_))
        print('決定係数 R^2： ', model_lr.score(x, y))

        return 'teest'
