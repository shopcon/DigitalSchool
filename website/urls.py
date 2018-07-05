from django.conf.urls import patterns, include, url


urlpatterns=[
    url(r'sandip-gund/$', 'website.views.theperson', name='ThePerson View'),
    url(r'mission-digital-school/$', 'website.views.theperson2', name='Mission Digital School View'),
    url(r'our-gallery/$', 'website.views.ourgallery', name='Our Gallery View'),
    url(r'photos/$', 'website.views.photogallery', name='Photo Gallery View'),

    url(r'media/$', 'website.views.mediagallery', name='Media Gallery View'),
    url(r'add-free-counselling/$', 'website.views.addfreecounselling', name='Add Free Counselling View'),
    url(r'blog/$', 'website.views.blog', name='Blog View'),

    url(r'blog/(?P<string1>\d+)/$', 'website.views.ind_blog', name='Individual Blog View'),

    url(r'^$', 'website.views.index_view', name='Index View'),
    url(r'^e-solutions/$', 'website.views.wesolutions', name='E-Solutions View'),

]