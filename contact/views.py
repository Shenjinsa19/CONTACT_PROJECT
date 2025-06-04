from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.cache import cache
from .tasks import send_contact_email

def contact_view(request):
    cached_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()

            # Trigger Celery task to send email asynchronously
            send_contact_email.delay(
                message.name,
                message.email,
                message.message
            )

            # Cache the user's message for 5 minutes keyed by email
            cache.set(f"user_msg_{message.email}", message.message, timeout=300)

            return redirect('contact_success')

    else:
        form = ContactForm()

        # If email query param exists, fetch cached message from Redis
        email = request.GET.get('email')
        if email:
            cached_message = cache.get(f"user_msg_{email}")

    return render(request, 'contact/contact_form.html', {
        'form': form,
        'cached_message': cached_message,
    })
