from django.shortcuts import render
from app1.forms import WorksForm, TopForm
from django.contrib.auth import authenticate, login, logout
import datetime
from app1.models import Works


def top(request):
    params = {'form': None}
    if request.method == 'POST':
        form = TopForm(request.POST)
        if 'login' in request.POST:
            name = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=name, password=password)
            # 認証に成功したらuserに名前が入り、失敗したらuserはnoneになる
            if user is not None:
                login(request, user)
                params['check'] = "ログインしました！"
            else:
                params['check'] = "ユーザー名またはパスワードが間違っています。"
        elif 'logout' in request.POST:
            logout(request)
            params['check'] = "ログアウトしました！"
        params['form'] = form
    else:
        params['form'] = TopForm()
    return render(request, 'top.html', params)


def work(request):
    params = {'form': WorksForm()}
    initial_dict = dict(name=request.user, date=datetime.date.today(),
                        in_time=datetime.time(9, 0, 0).strftime('%H:%M'),
                        out_time=datetime.datetime.now().strftime('%H:%M'),
                        rest_time=datetime.time(1, 0, 0).strftime('%H:%M'))
    if request.method == 'POST':
        form = WorksForm(request.POST)
        params['date'] = request.POST['date']
        if 'btn' in request.POST:
            w = Works.objects.filter(name=request.POST['name'], date=params['date'])
            if w.count() == 0:  # 追加
                w1 = Works(name=request.POST['name'], date=params['date'],
                           in_time=request.POST['in_time'], out_time=request.POST['out_time'],
                           rest_time=request.POST['rest_time'], other=request.POST['other'])
                w1.save()
                params['check'] = "追加しました!"

            elif w.count() == 1:  # 変更
                w = Works.objects.get(name=request.POST['name'], date=params['date'])
                w.in_time = request.POST['in_time']
                w.out_time = request.POST['out_time']
                w.rest_time = request.POST['rest_time']
                w.other = request.POST['other']
                w.save()
                params['check'] = "変更しました!"
            else:
                params['check'] = "エラーがあります。件数=" + str(w.count())

        # params['table2'] = Works.objects.annotate(total=)
        # params['total'] = Works.objects.annotate(
            # total=Sign(Sign(F('out_time') - F('in_time')) - F('rest_time')))
        params['form'] = form

    else:
        params['date'] = str(datetime.date.today())
        params['form'] = WorksForm(initial=initial_dict)

    # 表示する
    params['table'] = Works.objects.filter(
        name=request.user,
        date__year=params['date'][:4],
        date__month=params['date'][5:7]
    )
    params['test1'] = Works.objects.filter(
        name=request.user,
        date__year=params['date'][:4],
        date__month=params['date'][5:7]
    ).values_list('in_time', 'out_time', flat=False)
    time_sum = datetime.timedelta()
    datetime.datetime.strptime(datetime.time(9, 0, 0).strftime('%H:%M:%S'), '%H:%M:%S')
    for i in params['test1']:
        a = datetime.datetime.combine(datetime.date(2022, 1, 1), i[0])
        b = datetime.datetime.combine(datetime.date(2022, 1, 1), i[1])
        time_sum += b - a
    time_sum = time_sum / datetime.timedelta(hours=1)
    params['total'] = "名前:" + str(request.user) + "<br>出勤:" + str(round(time_sum, 1)) + "時間"
    return render(request, 'work.html', params)
