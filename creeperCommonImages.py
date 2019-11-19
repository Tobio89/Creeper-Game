import pygame, os, random

pygame.init()

baseImagePath = r'C:\Come On Python Games\resources\creeperGame\commonImages'
flashImagePath = r'C:\Come On Python Games\resources\creeperGame\flashImages'

backgroundImage = pygame.image.load(os.path.join(baseImagePath, 'background.png'))


menuButtonsPath = r'C:\Come On Python Games\resources\creeperGame\commonImages\menuButtons' 
menuButtons = {
    'BookMenu': 
                {
            'BookMenuCO' : pygame.image.load(os.path.join(menuButtonsPath, 'BookMenuCO.png')),
            'BookMenuEB' : pygame.image.load(os.path.join(menuButtonsPath, 'BookMenuEB.png'))
                },
    
    'COMenu': 
                {    
            'CO1Button'  : pygame.image.load(os.path.join(menuButtonsPath, 'CO1Button.png')),
            'CO2Button'  : pygame.image.load(os.path.join(menuButtonsPath, 'CO2Button.png')),
            'CO3Button'  : pygame.image.load(os.path.join(menuButtonsPath, 'CO3Button.png')),
            'CO4Button'  : pygame.image.load(os.path.join(menuButtonsPath, 'CO4Button.png'))
                },
    
    'EBMenu':
                {
            'EB2Button' : pygame.image.load(os.path.join(menuButtonsPath, 'EB2Button.png')),
            'EB3Button' : pygame.image.load(os.path.join(menuButtonsPath, 'EB3Button.png')),
            'EB4Button' : pygame.image.load(os.path.join(menuButtonsPath, 'EB4Button.png'))            
                },    
}

houseBasePath = r'C:\Come On Python Games\resources\creeperGame\commonImages\houseBase'
houseBase = [
    pygame.image.load(os.path.join(houseBasePath, 'houseBase_000.png')),
    pygame.image.load(os.path.join(houseBasePath, 'houseBase_001.png')),
    pygame.image.load(os.path.join(houseBasePath, 'houseBase_002.png')),
    pygame.image.load(os.path.join(houseBasePath, 'houseBase_003.png')),
]



houseStatePath = r'C:\Come On Python Games\resources\creeperGame\commonImages\houseState' 
houseState = [
    pygame.image.load(os.path.join(houseStatePath, 'houseState_000.png')),
    pygame.image.load(os.path.join(houseStatePath, 'houseState_001.png')),
    pygame.image.load(os.path.join(houseStatePath, 'houseState_002.png')),
    pygame.image.load(os.path.join(houseStatePath, 'houseState_003.png')),
    pygame.image.load(os.path.join(houseStatePath, 'houseState_004.png')),
]



winnerPath = r'C:\Come On Python Games\resources\creeperGame\commonImages\winner'
winner = {
    'teamA' : pygame.image.load(os.path.join(winnerPath, 'winTileA.png')),
    'teamB' : pygame.image.load(os.path.join(winnerPath, 'winTileB.png')),
    'both'  : pygame.image.load(os.path.join(winnerPath, 'winTileAll.png'))
} 


explosionSeqPath = r'C:\Come On Python Games\resources\creeperGame\commonImages\explosionSeq'
explosionFiles = [(os.path.join(explosionSeqPath, pngFile)) for pngFile in os.listdir(explosionSeqPath) if os.path.splitext(pngFile)[1] == '.png']
explosionSeq = [pygame.image.load(image) for image in explosionFiles]


teamTurnIndicator = {
    'teamA' : pygame.image.load(os.path.join(baseImagePath, 'teamATurnIndicator.png' )),
    'teamB' : pygame.image.load(os.path.join(baseImagePath, 'teamBTurnIndicator.png' ))
}

blockTiles = {
    'creeper' : pygame.image.load(os.path.join(baseImagePath, 'creeperHead.png' )),
    'cobble' : pygame.image.load(os.path.join(baseImagePath, 'cobbleStone.png' ))
}

remainingIcons = {
    'creeper' : pygame.image.load(os.path.join(baseImagePath, 'creepersRemainingIcon.png' )),
    'cobble' : pygame.image.load(os.path.join(baseImagePath, 'blocksRemainingIcon.png' ))
}

frameImg = pygame.image.load(os.path.join(baseImagePath, 'frame.png' ))

flashImagePaths = {
    'CO1' : {
        'u1' : os.path.join(flashImagePath, 'CO1', 'u1'),
        'u2' : os.path.join(flashImagePath, 'CO1', 'u2'),
        'u3' : os.path.join(flashImagePath, 'CO1', 'u3'),
        'u4' : os.path.join(flashImagePath, 'CO1', 'u4'),
        'u5' : os.path.join(flashImagePath, 'CO1', 'u5'),
        'u6' : os.path.join(flashImagePath, 'CO1', 'u6'),
        'u7' : os.path.join(flashImagePath, 'CO1', 'u7'),
        'u8' : os.path.join(flashImagePath, 'CO1', 'u8')
        },
    'CO2' : {
        'u1' : os.path.join(flashImagePath, 'CO2', 'u1'),
        'u2' : os.path.join(flashImagePath, 'CO2', 'u2'),
        'u3' : os.path.join(flashImagePath, 'CO2', 'u3'),
        'u4' : os.path.join(flashImagePath, 'CO2', 'u4'),
        'u5' : os.path.join(flashImagePath, 'CO2', 'u5'),
        'u6' : os.path.join(flashImagePath, 'CO2', 'u6'),
        'u7' : os.path.join(flashImagePath, 'CO2', 'u7'),
        'u8' : os.path.join(flashImagePath, 'CO2', 'u8')
        }, 
    'CO3' : {
        'u1' : os.path.join(flashImagePath, 'CO3', 'u1'),
        'u2' : os.path.join(flashImagePath, 'CO3', 'u2'),
        'u3' : os.path.join(flashImagePath, 'CO3', 'u3'),
        'u4' : os.path.join(flashImagePath, 'CO3', 'u4'),
        'u5' : os.path.join(flashImagePath, 'CO3', 'u5'),
        'u6' : os.path.join(flashImagePath, 'CO3', 'u6'),
        'u7' : os.path.join(flashImagePath, 'CO3', 'u7'),
        'u8' : os.path.join(flashImagePath, 'CO3', 'u8')
        }, 
    'CO4' : {
        'u1' : os.path.join(flashImagePath, 'CO4', 'u1'),
        'u2' : os.path.join(flashImagePath, 'CO4', 'u2'),
        'u3' : os.path.join(flashImagePath, 'CO4', 'u3'),
        'u4' : os.path.join(flashImagePath, 'CO4', 'u4'),
        'u5' : os.path.join(flashImagePath, 'CO4', 'u5'),
        'u6' : os.path.join(flashImagePath, 'CO4', 'u6'),
        'u7' : os.path.join(flashImagePath, 'CO4', 'u7'),
        'u8' : os.path.join(flashImagePath, 'CO4', 'u8')
        },  
    'EB2' : {
        'u1' : os.path.join(flashImagePath, 'EB2', 'u1'),
        'u2' : os.path.join(flashImagePath, 'EB2', 'u2'),
        'u3' : os.path.join(flashImagePath, 'EB2', 'u3'),
        'u4' : os.path.join(flashImagePath, 'EB2', 'u4'),
        'u5' : os.path.join(flashImagePath, 'EB2', 'u5'),
        'u6' : os.path.join(flashImagePath, 'EB2', 'u6'),
        'u7' : os.path.join(flashImagePath, 'EB2', 'u7'),
        'u8' : os.path.join(flashImagePath, 'EB2', 'u8')
        },
    'EB3' : {
        'u1' : os.path.join(flashImagePath, 'EB3', 'u1'),
        'u2' : os.path.join(flashImagePath, 'EB3', 'u2'),
        'u3' : os.path.join(flashImagePath, 'EB3', 'u3'),
        'u4' : os.path.join(flashImagePath, 'EB3', 'u4'),
        'u5' : os.path.join(flashImagePath, 'EB3', 'u5'),
        'u6' : os.path.join(flashImagePath, 'EB3', 'u6'),
        'u7' : os.path.join(flashImagePath, 'EB3', 'u7'),
        'u8' : os.path.join(flashImagePath, 'EB3', 'u8')
        },
    'EB4' : {
        'u1' : os.path.join(flashImagePath, 'EB4', 'u1'),
        'u2' : os.path.join(flashImagePath, 'EB4', 'u2'),
        'u3' : os.path.join(flashImagePath, 'EB4', 'u3'),
        'u4' : os.path.join(flashImagePath, 'EB4', 'u4'),
        'u5' : os.path.join(flashImagePath, 'EB4', 'u5'),
        'u6' : os.path.join(flashImagePath, 'EB4', 'u6'),
        'u7' : os.path.join(flashImagePath, 'EB4', 'u7'),
        'u8' : os.path.join(flashImagePath, 'EB4', 'u8')
        }
}

def getImageFilesFromPath(bookVer, unit):
    return [os.path.join(flashImagePaths[bookVer][unit], image) for image in os.listdir(flashImagePaths[bookVer][unit]) if os.path.splitext(image)[1] == '.png']


flashImages = {
    'CO1' : {
        'u1' : getImageFilesFromPath('CO1', 'u1'),
        'u2' : getImageFilesFromPath('CO1', 'u2'),
        'u3' : getImageFilesFromPath('CO1', 'u3'),
        'u4' : getImageFilesFromPath('CO1', 'u4'),
        'u5' : getImageFilesFromPath('CO1', 'u5'),
        'u6' : getImageFilesFromPath('CO1', 'u6'),
        'u7' : getImageFilesFromPath('CO1', 'u7'),
        'u8' : getImageFilesFromPath('CO1', 'u8')
        },
    'CO2' : {
        'u1' : getImageFilesFromPath('CO2', 'u1'),
        'u2' : getImageFilesFromPath('CO2', 'u2'),
        'u3' : getImageFilesFromPath('CO2', 'u3'),
        'u4' : getImageFilesFromPath('CO2', 'u4'),
        'u5' : getImageFilesFromPath('CO2', 'u5'),
        'u6' : getImageFilesFromPath('CO2', 'u6'),
        'u7' : getImageFilesFromPath('CO2', 'u7'),
        'u8' : getImageFilesFromPath('CO2', 'u8')
        },
    'CO3' : {
        'u1' : getImageFilesFromPath('CO3', 'u1'),
        'u2' : getImageFilesFromPath('CO3', 'u2'),
        'u3' : getImageFilesFromPath('CO3', 'u3'),
        'u4' : getImageFilesFromPath('CO3', 'u4'),
        'u5' : getImageFilesFromPath('CO3', 'u5'),
        'u6' : getImageFilesFromPath('CO3', 'u6'),
        'u7' : getImageFilesFromPath('CO3', 'u7'),
        'u8' : getImageFilesFromPath('CO3', 'u8')
        },
    'CO4' : {
        'u1' : getImageFilesFromPath('CO4', 'u1'),
        'u2' : getImageFilesFromPath('CO4', 'u2'),
        'u3' : getImageFilesFromPath('CO4', 'u3'),
        'u4' : getImageFilesFromPath('CO4', 'u4'),
        'u5' : getImageFilesFromPath('CO4', 'u5'),
        'u6' : getImageFilesFromPath('CO4', 'u6'),
        'u7' : getImageFilesFromPath('CO4', 'u7'),
        'u8' : getImageFilesFromPath('CO4', 'u8')
        },
    'EB2' : {
        'u1' : getImageFilesFromPath('EB2', 'u1'),
        'u2' : getImageFilesFromPath('EB2', 'u2'),
        'u3' : getImageFilesFromPath('EB2', 'u3'),
        'u4' : getImageFilesFromPath('EB2', 'u4'),
        'u5' : getImageFilesFromPath('EB2', 'u5'),
        'u6' : getImageFilesFromPath('EB2', 'u6'),
        'u7' : getImageFilesFromPath('EB2', 'u7'),
        'u8' : getImageFilesFromPath('EB2', 'u8')
        },
    'EB3' : {
        'u1' : getImageFilesFromPath('EB3', 'u1'),
        'u2' : getImageFilesFromPath('EB3', 'u2'),
        'u3' : getImageFilesFromPath('EB3', 'u3'),
        'u4' : getImageFilesFromPath('EB3', 'u4'),
        'u5' : getImageFilesFromPath('EB3', 'u5'),
        'u6' : getImageFilesFromPath('EB3', 'u6'),
        'u7' : getImageFilesFromPath('EB3', 'u7'),
        'u8' : getImageFilesFromPath('EB3', 'u8')
        },
    'EB4' : {
        'u1' : getImageFilesFromPath('EB4', 'u1'),
        'u2' : getImageFilesFromPath('EB4', 'u2'),
        'u3' : getImageFilesFromPath('EB4', 'u3'),
        'u4' : getImageFilesFromPath('EB4', 'u4'),
        'u5' : getImageFilesFromPath('EB4', 'u5'),
        'u6' : getImageFilesFromPath('EB4', 'u6'),
        'u7' : getImageFilesFromPath('EB4', 'u7'),
        'u8' : getImageFilesFromPath('EB4', 'u8')
        }
}




def fetchImage(path):
    return pygame.image.load(path)

def fetchImages(bookVer, unit1, unit2):

    firstUnitImages = flashImages[bookVer][unit1]
    secondUnitImages = flashImages[bookVer][unit2]

    random.shuffle(firstUnitImages)
    random.shuffle(secondUnitImages)

    if len(firstUnitImages) > 8 and len(secondUnitImages) > 8:
        selectedImagePaths = firstUnitImages[:8] + secondUnitImages[:8]
    elif len(firstUnitImages) < 8:
        offset = 16 - len(firstUnitImages)
        selectedImagePaths = firstUnitImages + secondUnitImages[:offset]
    elif len(secondUnitImages) < 8:
        offset = 16 - len(secondUnitImages)
        selectedImagePaths = firstUnitImages[:offset] + secondUnitImages


    pygameImages = []
    for path in selectedImagePaths:
        pygameImages.append(pygame.image.load(path))
    random.shuffle(pygameImages)


    rowA = pygameImages[0:4]
    rowB = pygameImages[4:8]
    rowC = pygameImages[8:12]
    rowD = pygameImages[12:16]

    return [rowA, rowB, rowC, rowD]

def fetchRandomImagesFromChosenBook(bookVer):
    units = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8']

    chosenImages = []
    while len(chosenImages) < 16:
        chosenUnit = random.choice(units)
        chosenImages.append(random.choice(flashImages[bookVer][chosenUnit]))

    pygameImages = [fetchImage(imagePath) for imagePath in chosenImages]

    random.shuffle(pygameImages)
    
    rowA = pygameImages[0:4]
    rowB = pygameImages[4:8]
    rowC = pygameImages[8:12]
    rowD = pygameImages[12:16]
    return [rowA, rowB, rowC, rowD]

def fetchRandomImagesFromSeries(series):
    if series == 'CO':
        bookList = ['CO1', 'CO2', 'CO3', 'CO4']
    elif series == 'EB':
        bookList = ['EB2', 'EB3', 'EB4']

    units = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8']

    chosenImages = []
    while len(chosenImages) < 16:
        chosenBook = random.choice(bookList)
        chosenUnit = random.choice(units)
        chosenImages.append(random.choice(flashImages[chosenBook][chosenUnit]))
    
    pygameImages = [fetchImage(imagePath) for imagePath in chosenImages]

    random.shuffle(pygameImages)
    
    rowA = pygameImages[0:4]
    rowB = pygameImages[4:8]
    rowC = pygameImages[8:12]
    rowD = pygameImages[12:16]
    return [rowA, rowB, rowC, rowD]


print(fetchRandomImagesFromSeries('EB'))
