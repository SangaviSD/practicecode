from django.shortcuts import render
# from django.http import HttpResponse

# def hello(request):
    # return HttpResponse("hello hello World")
    # return render(request,"home.html",{'title':'django'})
    # return render(request,"base.html",{'name':'sangavi'})

def input_numbers(request):
    return render(request, 'input.html')

def add_numbers(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        name = request.POST.get('name')


        try:
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)

            # if name == 'add':
            #     result = num1 + num2
            #     operation = "Addition"

            # elif name == 'sub':
            #     result = num1 - num2
            #     operation = "Substraction"

            # elif name == 'mul':
            #     result = num1 * num2
            #     operation = "Multiplication"

            # elif name == 'div':
            #     result = num1 / num2
            #     operation = "Division"

            if name == 'sim':
                result = (num1 * num2 * num3) //100
                operation = "Simple Interest"

            else:
                result = 'invalid operation'

        except (TypeError , ValueError):
            result = "invalid input"
            print("invalid input")

        return render(request, 'result.html', {'num1': num1,'num2': num2, 'num3':num3, 'result': result, 'name':name,'operation':operation})
    else:
        return render(request, 'input.html')