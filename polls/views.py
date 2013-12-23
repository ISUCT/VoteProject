from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from polls.models import Poll, Choice
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse


#def test(request):
    ##print((request))
    #print(request.GET)
    ##a=int(request.GET['a'])
    ##b=int(request.GET['b'])
    ##print("summ",a+b)

    #test3=""
    #if request.method=='POST':
        #Ael = request.POST.get("A","emptyyy")
        #Bel = request.POST.get("B","emptyyy")
        #print(Ael,Bel)
        #test3 =float(Ael) + float(Bel)
    #print "test right now"
    #text = "hello django"
    #text2 = "hello again"
    #return render(request,'polls/test.html', {'some': text,'some_2':text2,'result':test3})


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
    #return HttpResponse(output)

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
        #return HttpResponseRedirect(reverse('polls/results', kwargs={'object_id': p.id}))
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
