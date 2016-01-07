# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
#from myproject.myapp.models import Event
#from myproject.myapp.models import Person
#from myproject.myapp.models import Document.*
from myproject.myapp.forms import DocumentForm
from myproject.myapp.forms import SharedWith
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from myproject.myapp.forms import UserForm
from django.shortcuts import render

from django.contrib.auth import logout

#from django.utils.encoding import smart_str

#response = HttpResponse(mimetype='application/force-download')
#response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
#response['X-Sendfile'] = smart_str(path_to_file)
# It's usually a good idea to set the 'Content-Length' header too.
# You can also set any other required headers: Cache-Control, etc.
#return response

@login_required
def list(request):

        
 
    # Load documents for the list page
 #   d1=Document()
  #  documents = d1.get_my_files(request.user)
    documents = Document.objects.filter(user=request.user)
#    shared_doc = Document.objects.filter(user=request.user)
 #   shared_doc=Document.objects.filter(event__to_user=request.user)
   # sharing.objects.filter(shared_user=request.user)    #filter(shared_file= ,shared_user= )
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'username':request.user },
        context_instance=RequestContext(request)
    )

def upload_files(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'],user=request.user)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()
        
 
    # Load documents for the list page
 #   d1=Document()
  #  documents = d1.get_my_files(request.user)
    documents = Document.objects.filter(user=request.user)
#    shared_doc = Document.objects.filter(user=request.user)
 #   shared_doc=Document.objects.filter(event__to_user=request.user)
   # sharing.objects.filter(shared_user=request.user)    #filter(shared_file= ,shared_user= )
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form,  'username':request.user },
        context_instance=RequestContext(request)
    )

def share(request):
    shared=SharedWith(request.POST,request.FILES)
    if shared.is_valid():
#            my_sharing=sharing.objects.create(shared_user=shared_user)
#            my_document=Document.object.create(docfile=request.FILES['shared_file'],user=shared_user)
#            my_sharing.shared_file.add(my_document)
         #   sharedfile=shared.cleaned_data['shared_file']:
          #  if sharedfile
        # print yes
          #  new_shared=sharing(shared_file=request.POST.get('sharedfile'),shared_users=request.POST['shared_user'])
          #  new_shared.save()
        return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            #print shared.cleaned_data['files']
            #print shared.cleaned_data['users']
 
    #        if 
    #        shared=sharing(share=reqest.FILES['share'])
    #        shared.save()
    else:
        shared=SharedWith() # A empty, unbound form


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
      
        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()


            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()


    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/myapp/list/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/myapp/login/')