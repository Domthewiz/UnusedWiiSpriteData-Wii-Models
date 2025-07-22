# Unused Wii Actors
# Custom Miyamoto sprites.py Module
# Sprites Images


from PyQt5 import QtCore, QtGui
Qt = QtCore.Qt

import spritelib as SLib

ImageCache = SLib.ImageCache


class SpriteImage_ActorSpawner(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['actor'],
            (0, -240),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('actor', 'Actor_Spawner.png')
class SpriteImage_TiltGirder(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['girder'],
            (0, -16.7),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('girder', 'tilt_girder.png')
class SpriteImage_PropellerBlock(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['blockflye'],
            (-1.866, -6.13),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('blockflye', 'block_fly.png')
        
class SpriteImage_Crowber(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['crowbere'],
            (-8, -2),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('crowbere', 'crowber.png')
class SpriteImage_LiftTaru(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['tarue'],
            (-16, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('tarue', 'lift_taru.png')
        SLib.loadIfNotInImageCache('tarul', 'lift_taru_large.png')
        
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
         
        if style == 0:
            self.image = ImageCache['tarue']

            self.xOffset = -16
            self.yOffset = 0   

        else:
            self.image = ImageCache['tarul']

            self.xOffset = -40
            self.yOffset = -24
            

        super().dataChanged()
    
class SpriteImage_FakeActor(SLib.SpriteImage_Static):  # 727
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('w0', 'w0.png')
        SLib.loadIfNotInImageCache('w1', 'w1.png')
        SLib.loadIfNotInImageCache('w2', 'w2.png')
        SLib.loadIfNotInImageCache('w3', 'w3.png')
        SLib.loadIfNotInImageCache('w4', 'w4.png')
        SLib.loadIfNotInImageCache('w5', 'w5.png')
        SLib.loadIfNotInImageCache('w6', 'w6.png')
        SLib.loadIfNotInImageCache('w7', 'w7.png')
        SLib.loadIfNotInImageCache('w8', 'w8.png')
        SLib.loadIfNotInImageCache('w9', 'w9.png')
        SLib.loadIfNotInImageCache('wa', 'wa.png')
        SLib.loadIfNotInImageCache('wb', 'wb.png')
        SLib.loadIfNotInImageCache('wc', 'wc.png')
        SLib.loadIfNotInImageCache('wd', 'wd.png')
        SLib.loadIfNotInImageCache('we', 'we.png')
        SLib.loadIfNotInImageCache('wf', 'wf.png')
          
    def dataChanged(self):
        style = self.parent.spritedata[8] & 0xF
         
        if style == 0:
            self.image = ImageCache['w0']

            self.xOffset = 0
            self.yOffset = 0

        elif style == 1:
            self.image = ImageCache['w1']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 2:
            self.image = ImageCache['w2']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 3:
            self.image = ImageCache['w3']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 4:
            self.image = ImageCache['w4']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 5:
            self.image = ImageCache['w5']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 6:
            self.image = ImageCache['w6']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 7:
            self.image = ImageCache['w7']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 8:
            self.image = ImageCache['w8']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 9:
            self.image = ImageCache['w9']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 10:
            self.image = ImageCache['wa']

            self.xOffset = 0
            self.yOffset = 0
        elif style == 11:
            self.image = ImageCache['wb']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 12:
            self.image = ImageCache['wc']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 13:
            self.image = ImageCache['wd']

            self.xOffset = 0
            self.yOffset = 0
        
        elif style == 14:
            self.image = ImageCache['we']

            self.xOffset = 0
            self.yOffset = 0
        
        else:
            self.image = ImageCache['wf']

            self.xOffset = 0
            self.yOffset = 0
            

        super().dataChanged()

ImageClasses = {
    360: SpriteImage_ActorSpawner,
    358: SpriteImage_FakeActor,
    345: SpriteImage_TiltGirder,
    202: SpriteImage_PropellerBlock,
    529: SpriteImage_Crowber,
    522: SpriteImage_LiftTaru
}