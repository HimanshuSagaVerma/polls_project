import json
from django.shortcuts import render
from django.http import HttpResponse
from polls_app.models import Polls, Profile
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def page(request, page_no):
    # print('value of page_no: ', page_no)
    # return HttpResponse('this is my page no: {asdfasdf}'.format(
    #         ** {
    #             'asdfasdf': page_no
    #         }
    #     )
    # )

    return HttpResponse('this is my page no: %s' % page_no)


def pg(request, pge):
    return HttpResponse('This is page number: %s' % pge)


def my_first_api(request):
    my_response = {
        'name': 'Himanshu',
        'age': '23'
    }
    my_response = json.dumps(my_response)
    return HttpResponse(my_response)


def list_polls(request):
    all_polls = Polls.objects.all()
    my_response = []
    for i in all_polls:
        single_poll_dict = {}
        single_poll_dict['question'] = i.question
        # single_poll_dict['option1'] = i.option1
        # single_poll_dict['option2'] = i.option2
        # single_poll_dict['image'] = str(i.image)
        my_response.append(single_poll_dict)

    my_response = json.dumps(my_response)
    return HttpResponse(my_response)


def detail_polls(request, poll_id):
    domain_name = "http://localhost:8005/"
    poll_obj = Polls.objects.get(id=poll_id)
    single_poll_dict = {}
    single_poll_dict['question'] = poll_obj.question
    single_poll_dict['option1'] = poll_obj.option1
    single_poll_dict['option2'] = poll_obj.option2
    single_poll_dict['image'] = domain_name + 'media/' + str(poll_obj.image)
    my_response = json.dumps(single_poll_dict)
    return HttpResponse(my_response)


class StudentApi(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StudentApi, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        all_polls = Polls.objects.all()
        my_response = []
        for i in all_polls:
            single_poll_dict = {}
            single_poll_dict['question'] = i.question
            # single_poll_dict['option1'] = i.option1
            # single_poll_dict['option2'] = i.option2
            # single_poll_dict['image'] = str(i.image)
            my_response.append(single_poll_dict)

        my_response = json.dumps(my_response)
        return HttpResponse(my_response)

    def post(self, request):
        msg = 'i am in post method'
        print msg
        return HttpResponse(msg)

    def put(self, request):
        msg = 'i am in put method'
        print msg
        return HttpResponse(msg)

    def delete(self, request):
        msg = 'i am in delete method'
        print msg
        return HttpResponse(msg)


def list_all_polls_on_web(request):
    # return HttpResponse("adfasfsfas")
    template_name = "polls/list_all_polls_on_web.html"
    context = {}
    all_polls = Polls.objects.all()
    context['all_polls'] = all_polls
    return render(request, template_name, context)
    # return render(request, "polls/list_all_polls_on_web.html", {"all_polls": all_polls } )


def my_first_form(request):
    template_name = "polls/my_first_form.html"
    context = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print 'username is: %s' % username
        print 'password is: %s' % password 

        Profile.objects.create(
            username=username,
            password=password
        )
    return render(request, template_name, context)

