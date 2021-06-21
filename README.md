# My REST Service
 
1) Clone the repo.
2) In your terminal, in the repo, run `python manage.py runserver`
3) In your browser go to localhost:8000.
4) The service should be there and running.


# Notes

I was unable to get the word count feature up and running.  The QuerySet from Django I was trying to use to count wasn't JSON serialisable and that was a problem I just couldn't seem to overcome.  I'm sure its a simple solution I just didn't see, but thats what I was working with.
