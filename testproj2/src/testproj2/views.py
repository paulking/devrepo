from django.shortcuts import render_to_response
import models

def _GetUsers():
  return models.Person.objects.all()
  
def home(request):
  """The homepage view."""
  context = {
      'variable': 'foo2',
      'users': _GetUsers()} 
  return render_to_response(
      'index.html', context)
  
def user_edit(request):
  """The edit_user view."""
  context = {
      'users': _GetUsers()}      # need to fetch just desired user
  return render_to_response(
      'user_edit.html', context)
  
  