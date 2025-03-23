from django.shortcuts import render
from django.views import View
from .langchain import askproblem
from django.http import JsonResponse
from .forms import ProblemForm
import markdown

class Home(View):
    def get(self, request):
        # Retrieve the AI response from the session, if it exists
        ai_content = request.session.get('ai_content', '')
        return render(request, 'home.html', {'ai_content': ai_content})

    def post(self, request):
        form = ProblemForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Get the AI response using the askproblem function
            response = askproblem(query)
            # Convert the response to markdown format
            markdown_response = markdown.markdown(response, extensions=['fenced_code', 'codehilite'])
            # Store the markdown response in the session
            request.session['ai_content'] = markdown_response
            # Return the response as JSON
            return JsonResponse({'ai_content': markdown_response})
        # If the form is invalid, return an error response
        return JsonResponse({'error': 'Invalid form data'}, status=400)


# from django.shortcuts import render
# from django.views import View
# from .langchain import askproblem
# from django.http import JsonResponse
# from .forms import ProblemForm
# import markdown

# # Create your views here.

# class Home(View):
#     def get(self, request):
#         ai_content = request.session.get('ai_content', '')
#         return render(request, 'home.html' , {'ai_content': ai_content})

    
#     def post(self, request):
#         form = ProblemForm(request.POST)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             response = askproblem(query)
#             markdown_response = markdown.markdown(response, extensions=['fenced_dode', 'codehilite'])
#             request.session['ai_content'] = markdown_response
#         ai_content = request.session.get('ai_content', '')
#         return JsonResponse({'ai_content': ai_content})
    