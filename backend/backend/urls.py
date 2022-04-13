"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/author/list/', AuthorDAO.list),
    path('api/author/<int:id>', AuthorDAO.getById),
    path('api/author/create', AuthorDAO.create),
    path('api/author/update/<int:id>', AuthorDAO.update),
    path('api/author/delete/<int:id>', AuthorDAO.delete),
    path('api/publisher/list/', PublisherDAO.list),
    path('api/publisher/<int:id>', PublisherDAO.getById),
    path('api/publisher/create', PublisherDAO.create),
    path('api/publisher/update/<int:id>', PublisherDAO.update),
    path('api/publisher/delete/<int:id>', PublisherDAO.delete),
    path('api/categoryBook/list/', CategoryBookDAO.list),
    path('api/categoryBook/<int:id>', CategoryBookDAO.getById),
    path('api/categoryBook/create', CategoryBookDAO.create),
    path('api/categoryBook/update/<int:id>', CategoryBookDAO.update),
    path('api/categoryBook/delete/<int:id>', CategoryBookDAO.delete),
    path('api/book/list/', BookDAO.list),
    path('api/book/<int:id>', BookDAO.getById),
    path('api/book/create', BookDAO.create),
    path('api/book/update/<int:id>', BookDAO.update),
    path('api/book/delete/<int:id>', BookDAO.delete),
    path('api/bookItem/list/', BookItemDAO.list),
    path('api/bookItem/<int:id>', BookItemDAO.getById),
    path('api/bookItem/create', BookItemDAO.create),
    path('api/bookItem/update/<int:id>', BookItemDAO.update),
    path('api/bookItem/delete/<int:id>', BookItemDAO.delete),

]


