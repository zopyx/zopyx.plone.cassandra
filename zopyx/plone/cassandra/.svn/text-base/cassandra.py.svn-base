# -*- coding: utf-8 -*-
################################################################
# zopyx.plone.cassandra
#
# ZOPYX Limited & Co. KG
# Charlottenstr. 37/1, D-72070 Tübingen, Germany
# info@zopyx.com, www.zopyx.com 
################################################################

"""
zopyx.plone.cassandra
"""

from Globals import InitializeClass
from AccessControl import getSecurityManager
from Products.Five import BrowserView


class CassandraView(BrowserView):

    def test(self, cond, expr1,  expr2):
        if cond:
            return expr1
        return expr2

    def reportPermissions(self, filter=('local',)):
        """ Walk over all subfolders of the current folder and 
            get hold of local roles etc.
        """

        context_path = '/'.join(self.context.getPhysicalPath())
        brains = self.context.portal_catalog(path=context_path,
                                             is_folderish=True,
                                             )

        lst = []
        for brain in brains:
            folder = brain.getObject()
            rolemap = folder.computeRoleMap()

            _rolemap = []
            for d in rolemap:
                if not d['global']:
                    del d['global']

                if d['local'] == ('Owner',) or len(d['local']) == 0:
                    del d['local']

                if d['acquired'] == ('Owner',) or len(d['acquired']) == 0:
                    del d['acquired']

                if d.has_key('global') or d.has_key('local') or d.has_key('acquired'):
                    _rolemap.append(d)

            rel_path = '/'.join(folder.getPhysicalPath()).replace(context_path, '')
            if rel_path.startswith('/'):
                rel_path = rel_path[1:]
            if not rel_path:
                rel_path = ''

            if _rolemap:
                lst.append({ 'path' : brain.getURL(1),
                             'relative_path': rel_path,
                             'id ' : folder.getId(),
                             'title' : folder.Title(),
                             'rolemap' : _rolemap,
                          })

        lst.sort(lambda x,y: cmp(x['relative_path'], y['relative_path']))
        return lst

InitializeClass(CassandraView)
