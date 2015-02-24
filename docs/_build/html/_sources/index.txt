.. two_scope_of_django documentation master file, created by
   sphinx-quickstart on Tue Feb 24 00:56:44 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to two_scope_of_django's documentation!
===============================================

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Section Header
==============
**emphasis (bold/strong)**

*italics*

Simple link: http://django.2scoops.org

Fancier Link: `Two Scoops of Django`_

.. _`Two Scoops of Django`: https://django.2scoops.org

Subsecion Header
----------------

#) An enumerated list item

#) Second item

* First bullet

* Second bullet

  * Indented Bullet

  * Note carriage return and indents

Literal code block::
	
	def like():
		print("I like Ice Cream")
	
	for i in range(10):
		like()


Python colored code block (requires pygments):

.. code-block:: python

	# You need to "pip install pygments" to make this work.
	for i in range(10):
		like()

JavaScript colored code block:

.. code-block:: javascript

	console.log("Don't use alert()");