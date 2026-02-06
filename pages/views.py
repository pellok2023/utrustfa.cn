from django.shortcuts import render


def home(request):
    """首頁（青島又上企業服務官網）"""
    return render(request, 'pages/index.html')
