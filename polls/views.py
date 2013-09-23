from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from polls.models import Poll, Choice
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse


def test(request):
    print(dir(request.POST))    
    test3=""
    if request.method=='POST':
        inp = request.POST.get("inp","emptyyy")
        print(inp)			
        test3 = inp
    print "test"
    text = "hello"#"""<html><body><h1>Hello world</h1><p>asdfgvbasdbg</p></body></html>"""
    text2 = "hello again"
    return render(request,'polls/test.html', {'some': text,'some_2':text2,'result':test3})


def index(request):
    print "index"
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def results(request, poll_id):
    print "result"
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def detail(request, poll_id):
    print "detail"
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def vote(request, poll_id):
    print "vote"
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', kwargs={'object_id': p.id}))
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
