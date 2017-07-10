# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/PECamManager/__init__.py
from os import environ
from gettext import bindtextdomain, dgettext, gettext
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

def localeInit():
    environ['LANGUAGE'] = language.getLanguage()[:2]
    bindtextdomain('PECamManager', resolveFilename(SCOPE_PLUGINS, 'Extensions/PECamManager/locale'))


def _(txt):
    t = dgettext('PECamManager', txt)
    if t == txt:
        t = gettext(txt)
    return t


localeInit()
language.addCallback(localeInit)