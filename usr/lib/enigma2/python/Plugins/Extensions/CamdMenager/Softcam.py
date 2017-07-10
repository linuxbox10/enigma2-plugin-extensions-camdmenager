# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/CamdMenager/Softcam.py
from os import mkdir, path, remove
from Components.config import config
from Components.Console import Console

def getcamcmd(cam):
    camname = cam.lower()
    if getcamscript(camname):
        return config.plugins.Camd.camdir.value + '/' + cam + ' start'
    return config.plugins.Camd.camdir.value + '/' + cam


def getcamscript(cam):
    cam = cam.lower()
    if cam[-3:] == '.sh' or cam[:7] == 'softcam' or cam[:10] == 'cardserver':
        return True
    return False


def stopcam(cam):
    if getcamscript(cam):
        cmd = config.plugins.Camd.camdir.value + '/' + cam + ' stop'
    else:
        cmd = 'killall -9 ' + cam
    Console().ePopen(cmd)
    try:
        remove('/tmp/ecm.info')
    except:
        pass


def __createdir(list):
    dir = ''
    for line in list[1:].split('/'):
        dir += '/' + line
        if not path.exists(dir):
            try:
                mkdir(dir)
            except:
                print '[Camd Menager] Failed to mkdir', dir


def checkconfigdir():
    if not path.exists(config.plugins.Camd.camconfig.value):
        __createdir('/usr/keys')
        config.plugins.Camd.camconfig.value = '/usr/keys'
        config.plugins.Camd.camconfig.save()
    if not path.exists(config.plugins.Camd.camdir.value):
        __createdir('/usr/camd')
        config.plugins.Camd.camdir.value = '/usr/camd'
        config.plugins.Camd.camdir.save()