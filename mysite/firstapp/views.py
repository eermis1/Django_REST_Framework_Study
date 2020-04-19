from actstream import models
from actstream.models import user_stream, Action
from actstream.models import any_stream
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from actstream.models import user_stream

USER_MODEL = get_user_model()

def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index.")

def stream(request):

    return render(request, 'stream.html',
                  context={
            'ctype': ContentType.objects.get_for_model(USER_MODEL),
            'actor': request.user,
            'action_list': models.user_stream(request.user)
        }
    )

def model(request, content_type_id):
    """
    ``Actor`` focused activity stream for actor defined by ``content_type_id``,
    ``object_id``.
    """
    ctype = get_object_or_404(ContentType, pk=content_type_id)
    model_class = ctype.model_class()
    return render(
        request,
        'model_stream.html',
        {
            'action_list': models.model_stream(model_class),
            'ctype': ctype,
            'actor': model_class
        }
    )

# Follow Links
# http://127.0.0.1:8000/activity/follow/<content_type_id>/<object_id>/
# http://127.0.0.1:8000/activity/follow_all/<content_type_id>/<object_id>/
# Content Type Id = 4 --> User, 8 --> Community, 12 --> Post