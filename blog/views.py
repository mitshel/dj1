from django.shortcuts import render
from django.utils import timezone
from blog.models import DashaPost

# Create your views here.

def BlogList(request):
	posts = DashaPost.objects.all()
	args = {}
	args['posts'] = posts
	args['param'] = 'pampam'
	args['post'] = posts[0]
	return render(request,'blog_list.html', args)

def BlogSend(request):
	if request.method == "POST":
		title = request.POST.get('title', '')
		body = request.POST.get('body', '')
		p = DashaPost()
		p.title = title
		p.body = body
		p.timestamp = timezone.now()
		p.save()

	return BlogList(request)


def BlogDel(request, id):
	d = DashaPost.objects.get(id=id)
	d.delete()

	return BlogList(request)