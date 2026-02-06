"""
URL configuration for utrustfa project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

# 提供靜態檔案服務（開發環境或未使用 Web 伺服器時）
if settings.DEBUG:
    # 優先從 STATIC_ROOT 提供（如果已執行 collectstatic）
    if settings.STATIC_ROOT.exists():
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    else:
        # 否則從 STATICFILES_DIRS 提供
        for static_dir in settings.STATICFILES_DIRS:
            urlpatterns += static(settings.STATIC_URL, document_root=static_dir)
