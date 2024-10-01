from django.shortcuts import render, redirect
import pyshorteners
from django.contrib import messages

def url_shortener(request):
    if request.method == "POST":
        try:
            shortener = pyshorteners.Shortener()
            url = request.POST.get("url")
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Generated")
            request.session['short_url'] = short_url  # Store the short URL in the session
            request.session['url'] = url  # Store the original URL in the session
            return redirect('url_shortener')  # Redirect after success
        except Exception as e:
            messages.error(request, "An error occurred: " + str(e))
    
    # Get the short URL and original URL from the session to display them
    short_url = request.session.get('short_url', '')
    url = request.session.get('url', '')

    # Clear the session after using it
    if short_url:
        del request.session['short_url']
        del request.session['url']

    return render(request, "index.html", {"short_url": short_url, "url": url})
