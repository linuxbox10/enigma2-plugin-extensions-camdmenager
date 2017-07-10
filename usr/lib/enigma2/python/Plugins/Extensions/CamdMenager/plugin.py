# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/CamdMenager/plugin.py
from . import _
from Components.config import config, ConfigSubsection, ConfigText
from Plugins.Plugin import PluginDescriptor
from Softcam import checkconfigdir
from Manager import CamdMenager
config.plugins.Camd = ConfigSubsection()
config.plugins.Camd.actcam = ConfigText(default='none')
config.plugins.Camd.camconfig = ConfigText(default='/usr/keys', visible_width=100, fixed_size=False)
config.plugins.Camd.camdir = ConfigText(default='/usr/EmuCamd', visible_width=100, fixed_size=False)
checkconfigdir()

def main(session, **kwargs):
    session.open(CamdMenager)


EnigmaStart = False

def startcam(reason, **kwargs):
    global EnigmaStart
    if config.plugins.Camd.actcam.value != 'none':
        if reason == 0 and not EnigmaStart:
            from Startup import startcamonstart
            EnigmaStart = True
            startcamonstart.start()
        elif reason == 1:
            from Softcam import stopcam
            stopcam(config.plugins.Camd.actcam.value)


def Plugins(**kwargs):
    return [PluginDescriptor(name=_('Camd Menager'), description=_('Stop-Start-Restart Emulator'), where=[PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU], icon='cmanager.png', fnc=main), PluginDescriptor(where=PluginDescriptor.WHERE_AUTOSTART, needsRestart=True, fnc=startcam)]