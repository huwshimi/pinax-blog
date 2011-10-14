from django.conf.urls.defaults import *

from biblion.views import BlogList, BlogCreate


urlpatterns = patterns("",
    # url(r"^$", "biblion.views.blog_index", name="blog"),
    url(r"^$", BlogList.as_view(), name="blog_list"),
    url(r"^create/$", BlogCreate.as_view(), name="blog_create"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$", "biblion.views.blog_post_detail", name="blog_post"),
    url(r"^post/(?P<post_pk>\d+)/$", "biblion.views.blog_post_detail", name="blog_post_pk"),
    url(r"^(?P<slug>[-\w]+)/$", "biblion.views.blog_section_list", name="blog_section"),
)