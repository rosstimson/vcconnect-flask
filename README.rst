VCConnect-Flask
===============

A simple Flask_ app that allows `VC Connect`_ users such as a
volunteer centre to provide a web based community directory.

Configuration
-------------

The following environment variables need to be set for the app to
work.

- ``VCC_API_KEY``: `VC Connect`_ API key.
- ``SECRET_KEY``:  Random string of bytes needed for CSRF protection.

Generate ``SECRET_KEY``
~~~~~~~~~~~~~~~~~~~~~~~

You can use Python to generate random bytes for use as the
``SECRET_KEY`` like so:

::

   $ python

   >>> import os
   >>> os.urandom(24)
   b"\xee\xa8\xed\xc8t\xc1\x07f\x84'\x97-7\x08\xd0rd\x94\x0fz0U\x04\xde"

Take the byte string and set it as an environment variable with:

::

   $ export SECRET_KEY="\xee\xa8\xed\xc8t\xc1\x07f\x84'\x97-7\x08\xd0rd\x94\x0fz0U\x04\xde"

License
-------

VCConnect-Flask is released under the `Apache License 2.0`_.


.. _Flask: http://flask.pocoo.org
.. _VC Connect: http://www.vcconnect.org.uk
.. _Apache License 2.0: https://opensource.org/licenses/Apache-2.0
