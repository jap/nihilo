nihilo
======

This package allows you to do the fantastic import:

  >>> from nihilo import nihil

This is a nice object which behaves like None but does accept method calls.
Why would you want this?

So, we have:

  >>> a_dict = { 'who': 'Parmenides' }
  >>> print a_dict.get('who')
  Parmenides
  >>> print a_dict.get('where')
  None

But you might want to do:
  >>> a_dict.get('who').startswith('g')
  False
  >>> a_dict.get('where').startswith('g')
  Traceback (most recent call last):
  ...
  AttributeError: 'NoneType' object has no attribute 'startswith'

With nihil, you can do:
  >>> print a_dict.get('where', nihil).startswith('g')
  nihil()

Note that casting to bool returns false, so you can easily test..:

  >>> if a_dict.get('where', nihil).startwith('g'):
  ...   print "got it!"

nihil is very flexible, it will also allow you to call almost any method
and it will return itself:

  >>> nihil.foo.bar('quux', frop=True)
  nihil()

And remember, ex nihilo nihil fit.
