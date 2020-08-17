from django.shortcuts import render
from comnt.forms import CommentsForm
from comnt.models import Comments
from comnt.prediction import comment_prediction
# Create your views here.

def index(request):

    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)

        if form.is_valid():
            comment = form.cleaned_data['inp_comment']
            uname = form.cleaned_data['uname']
            result = comment_prediction(comment)
            form.result = result
            form.save(commit=False)
            op_dict = {
                'uname' : uname,
                'result' : result,

            }
            return render(request, 'comnt/prediction_page.html', context={'predictions' : op_dict})

        else:
            print('ERROR FORM INVALID')

    else:
        return render(request, 'comnt/index.html', context={'form': form})
