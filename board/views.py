from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator
from fcuser.models import Fcuser
from .models import Board
from .form import BoardForm
# Create your views here.
def board_detail(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')
    return render(request,'board_detail.html',{'board':board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # 로그인 한 사용자 세션에서 가져온다.
            user_id =request.session.get('user')
            ## 세션에서 가져온 아이디가 모델에 있는 지 비교한다.
            fcuser = Fcuser.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.writer   = fcuser
            board.save()
            return redirect('/board/list/')
    else:
       form = BoardForm()
    return render(request, "board_write.html", {'form':form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = request.GET.get('p',1)
    paginator = Paginator(all_boards,2)
    
    boards = paginator.get_page(page)
    return render(request,'board_list.html',{'boards':boards})