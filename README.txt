zopyx.plone.cassandra
=====================

This module helps you to analyze your current security settings - especially
local roles granted on some subfolder

Installation
------------

- add ``zopyx.plone.cassandra`` to the ``eggs`` and ``zcml``
  options of your buildout.cfg. 
- re-run buildout
- for new Plone sites: choose the zopyx.plone.cassandra extension profile
- for existing Plone sites: add zopyx.plone.cassandra from
  Add/remove modules within the Plone site setup

Usage
-----

Add ``/@@cassandra`` to the url of any object with your Plone site and
see what happens.

Note
----
This module should only be used on development systems since it might
reveal security related information to untrusted users.

Sources
-------
- https://github.com/zopyx/zopyx.plone.cassandra

Issue tracker
-------------
- https://github.com/zopyx/zopyx.plone.cassandra/issues

License
-------
This module is licensed under the Zope Public License (ZPL 2.1).

Contact
-------

| ZOPYX Ltd. 
| c/o Andreas Jung, 
| Charlottenstr. 37/1
| D-72070 Tuebingen, Germany
| E-mail: info at zopyx dot com
| Web: http://www.zopyx.com

