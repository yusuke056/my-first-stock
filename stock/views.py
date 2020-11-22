from django.shortcuts import render

def post_list(request):
    return render(request, 'stock/post_list.html', {})