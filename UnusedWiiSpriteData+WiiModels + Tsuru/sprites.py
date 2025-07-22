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
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('actor', 'Actor_Spawner.png')


class SpriteImage_MassiveSpikedStake(SLib.SpriteImage_Static):  # 377
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MassiveSpikedStake'],
            (-98, -2445),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('MassiveSpikedStake', 'massive_stake_down_e_0.png')


class SpriteImage_MortyMole(SLib.SpriteImage_Static):  # 692
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['mortymole'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('mortymole', 'mortymole.png')


class SpriteImage_Parabones(SLib.SpriteImage_Static):  # 725
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Parabones'],
            (0, -6),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Parabones', 'Parabones.png')

   
class SpriteImage_Cataquack(SLib.SpriteImage_Static):  # 733
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Cataquack'],
            (-10, -19),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Cataquack', 'cataquack.png')


class SpriteImage_RainbowLight(SLib.SpriteImage_Static):  # 738
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['RainbowLight'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('RainbowLight', 'light.png')


class SpriteImage_CustomDoor(SLib.SpriteImage_Static):  # 726
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['CustomDoor'],
            (-16, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CustomDoor', 'customdoor.png')


class SpriteImage_TimeClock(SLib.SpriteImage_Static):  # 734
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['TimeClock'],
            (-16, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TimeClock', 'time_clock.png')

class SpriteImage_FakeActor(SLib.SpriteImage_Static):  # 727
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('fake_midway', 'fake_midwayflag.png')
        SLib.loadIfNotInImageCache('fake_goalpoal', 'fake_goalpoal.png')
        SLib.loadIfNotInImageCache('fake_starcoin', 'fake_starcoin.png')
          
    def dataChanged(self):
        style = self.parent.spritedata[5] & 0xF
         
        if style == 1:
            self.image = ImageCache['fake_goalpoal']

            self.xOffset = -36
            self.yOffset = -160

        elif style == 2:
            self.image = ImageCache['fake_starcoin']

            self.xOffset = -16
            self.yOffset = -16
        else:
            self.image = ImageCache['fake_midway']

            self.xOffset = -8
            self.yOffset = -56
            

        super().dataChanged()

        
class SpriteImage_Scuttlebug(SLib.SpriteImage_Static):  # 749
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['scuttlebug'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('scuttlebug', 'scuttlebug.png')
    
class SpriteImage_Biddybud(SLib.SpriteImage_Static):  # 758
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Biddybud'],
            (-8, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Biddybud', 'biddybud_red.png')
        
class SpriteImage_BasaltBones(SLib.SpriteImage_Static):  # 760
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BasaltBones'],
            (-32, -40),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('BasaltBones', 'basaltbones.png')
        
class SpriteImage_TripleBlock(SLib.SpriteImage_Static):  # 766
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.xOffset = -16
        self.yOffset = -16

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TripleBlock_standard', 'triple_block_standard.png')
        SLib.loadIfNotInImageCache('TripleBlock_chika', 'triple_block_chika.png')
        SLib.loadIfNotInImageCache('TripleBlock_yougan', 'triple_block_yougan.png')
        SLib.loadIfNotInImageCache('TripleBlock_yougan2', 'triple_block_yougan2.png')
          
    def dataChanged(self):
        animationStyle = self.parent.spritedata[0] & 0xF
            
        if animationStyle == 1:
            self.image = ImageCache['TripleBlock_chika']

        elif animationStyle == 2:
            self.image = ImageCache['TripleBlock_yougan']

        elif animationStyle == 3:
            self.image = ImageCache['TripleBlock_yougan2']
    
        else:
            self.image = ImageCache['TripleBlock_standard']

        super().dataChanged()


class SpriteImage_Peepa(SLib.SpriteImage_StaticMultiple):  # 770 TODO: add different platform variations?
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.xOffset = 0

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PeepaWoodPlat', 'peepa_platform.png')
        SLib.loadIfNotInImageCache('Peepa', 'peepa.png')
          
    def dataChanged(self):
        has_platform = (self.parent.spritedata[0] >> 1) & 8       
        
        if has_platform == 0:
            self.image = ImageCache['Peepa']
            
        elif has_platform == 8:
            self.image = ImageCache['PeepaWoodPlat']
            self.xOffset = -24
            

        super().dataChanged()


class SpriteImage_StarCoinShard(SLib.SpriteImage_Static):  # 729
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['StarCoinShard'],
            (-8, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('StarCoinShard', 'star_coin_shard.png')
        
class SpriteImage_Kamiya(SLib.SpriteImage_Static):  # 743
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Kamiya'],
            (-24, -32),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Kamiya', 'kamiya.png')

class SpriteImage_BeepBlock(SLib.SpriteImage_Static):  # 730
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('beep_block_red', 'beep_block_red.png')
        SLib.loadIfNotInImageCache('beep_block_blue', 'beep_block_blue.png')
          
    def dataChanged(self):
        animationStyle = (self.parent.spritedata[0] >> 1) & 8
        
        if animationStyle == 8:
            self.image = ImageCache['beep_block_blue']
            
        else:
             self.image = ImageCache['beep_block_red']
            

        super().dataChanged()
        
             
class SpriteImage_Chestnut(SLib.SpriteImage_Static):  # 731
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Chestnut'],
            (-8, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Chestnut', 'chestnut.png')
        
class SpriteImage_Flaptor(SLib.SpriteImage_Static):  # 761
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Flaptor'],
            (-16, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Flaptor', 'flaptor.png')
        
class SpriteImage_ColdFuzzy(SLib.SpriteImage_Static):  # 753
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ColdFuzzy'],
            (-16, -16),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('ColdFuzzy', 'coldfuzzy.png')
        
class SpriteImage_ActrSpawner(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['acor'],
            (0, -240),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('acor', 'Actr_Spawner.png')
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
        
class SpriteImage_GlwBlock(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['blockglowe'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('blockglowe', 'glow_block.png')

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
        
class SpriteImage_KoopaCave(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['koopac'],
            (-112, -160),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('koopac', 'koopa_cave.png')
        
class SpriteImage_Metealbox(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

    def loadImages():
        SLib.loadIfNotInImageCache('teeny', 'teeny_lift.png')
        SLib.loadIfNotInImageCache('small', 'small_lift.png')
        SLib.loadIfNotInImageCache('big', 'big_lift.png')
        
    def dataChanged(self):
        style = self.parent.spritedata[8] & 0xF
         
        if style == 0:
            self.image = ImageCache['teeny']

            self.xOffset = 0
            self.yOffset = 0   
            
        elif style == 1:
            self.image = ImageCache['small']

            self.xOffset = 0
            self.yOffset = 0   

        else:
            self.image = ImageCache['big']

            self.xOffset = 0
            self.yOffset = 0
         
        super().dataChanged()
        
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
    724: SpriteImage_ActorSpawner,
    748: SpriteImage_MassiveSpikedStake,
    725: SpriteImage_Parabones,
    733: SpriteImage_Cataquack,
    738: SpriteImage_RainbowLight,
    726: SpriteImage_CustomDoor,
    727: SpriteImage_FakeActor,
    730: SpriteImage_BeepBlock,
    734: SpriteImage_TimeClock,
    749: SpriteImage_Scuttlebug,
    758: SpriteImage_Biddybud,
    760: SpriteImage_BasaltBones,
    770: SpriteImage_Peepa,
    729: SpriteImage_StarCoinShard,
    743: SpriteImage_Kamiya,
    731: SpriteImage_Chestnut,
    761: SpriteImage_Flaptor,
    753: SpriteImage_ColdFuzzy,
    766: SpriteImage_TripleBlock,
    360: SpriteImage_ActrSpawner,
    358: SpriteImage_FakeActor,
    345: SpriteImage_TiltGirder,
    202: SpriteImage_PropellerBlock,
    529: SpriteImage_Crowber,
    199: SpriteImage_GlwBlock,
    522: SpriteImage_LiftTaru,
    319: SpriteImage_Metealbox,
    267: SpriteImage_KoopaCave
}