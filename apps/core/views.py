from django.contrib.auth.views import LoginView


class LoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['doc_title'] = 'Autenticação'
        context['top_app_name'] = 'Autenticação'
        context['pt_h1'] = 'Login no sistema'
        context['pt_span'] = 'Entre com e-mail e senha'
        context['pt_breadcrumb2'] = 'Autenticação'
        return context
