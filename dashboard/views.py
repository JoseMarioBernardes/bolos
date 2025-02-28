# dashboard/views.py

from django.views.generic import TemplateView
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Count
from django.db.models.functions import TruncMonth
from sales.models import Sale

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Expressão que soma o preço do bolo + taxa de entrega
        total_expression = ExpressionWrapper(
            F('cake__preco') + F('taxa_entrega'),
            output_field=DecimalField()
        )

        # Agregando vendas por mês: total (somatório) e contagem de vendas
        sales_data = (
            Sale.objects
            .annotate(month=TruncMonth('data'))
            .values('month')
            .annotate(
                total=Sum(total_expression),  # Soma do preço + taxa de entrega
                count=Count('id')             # Contagem de vendas
            )
            .order_by('month')
        )

        # Disponibiliza os dados no contexto
        context['sales_by_month'] = sales_data
        return context
