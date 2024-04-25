import itertools
import os
import re
import sys
import time

import numpy as np
import skimage.io as io

pathPattern = r'script\.py$'
for arg in sys.argv:
    if re.search(pathPattern, arg):
        cwd = os.path.dirname(os.path.abspath(arg))
        break

if not 'input' in os.listdir(cwd): os.mkdir('input')
if not 'output' in os.listdir(cwd): os.mkdir('output')

inputPath = os.path.join(cwd, 'input')
outputPath = os.path.join(cwd, 'output')

print('Wiping outputs')
for imageFile in os.listdir(outputPath):
    os.remove(os.path.join(outputPath, imageFile))
   
inputContent = os.listdir(inputPath)
inputDirs = [content for content in inputContent if os.path.isdir(os.path.join(inputPath, content))]
inputDirs = [os.path.join(inputPath, dir) for dir in inputDirs]
inputDirs.sort()

imagesDirs = []
imageFormatPattern = r'\.png$'
for dir in inputDirs:
    dirContent = os.listdir(dir)
    dirContent.sort()
    imagesDirs.append([os.path.join(dir, content) for content in dirContent 
                       if re.search(imageFormatPattern, content)])

print('Reading inputs')
images = []
layersSize = []
for dir in imagesDirs:
    layerSizeCount = 0
    for image in dir:
        images.append(io.imread(image))
        layerSizeCount += 1
    layersSize.append(layerSizeCount)

layersPattern = [list(range(size)) for size in layersSize]
layersPattern = list(map(lambda layer: list(map(str, layer)), layersPattern))
imageCombinations = list(itertools.product(*layersPattern))
imageCombinations = [''.join(combination) for combination in imageCombinations]
imageCombinations = np.array(imageCombinations)

print('Generating images')
totalImgs = len(imageCombinations)
generatedImgs = 0
percentageConcluded = 0
initialTime = time.time()
lastTime = time.time()
print(f'{0}s - {generatedImgs}/{totalImgs} - {round(percentageConcluded)}%', end='\r')
for combination in imageCombinations:
    outputImage = np.zeros(images[0].shape)
    for layerNumber, combIndex  in enumerate(combination):
        imageIndex = int(combIndex) + sum(layersSize[:layerNumber])
        imageToAdd = images[imageIndex]
        mask = imageToAdd[:,:,3] != 0
        outputImage[mask] = imageToAdd[mask]
        outputImage = outputImage.astype('uint8')
        
    fileNamePrefix = ''
    for combIndex in combination:
        fileNamePrefix += f'{combIndex}-'
    fileNamePrefix = fileNamePrefix[:-1]
    fileName = f'{fileNamePrefix}.png'
    fileName = os.path.join(outputPath, fileName)
    io.imsave(fileName, outputImage)

    generatedImgs += 1
    percentageConcluded = (generatedImgs/totalImgs)*100
    elapsedTime = time.time()
    if time.time() - lastTime >= 1:
        lastTime = time.time()
        print(f'{round(elapsedTime - initialTime)}s - {generatedImgs}/{totalImgs} -',
              f'{round(percentageConcluded)}%', end='\r')
conclusionTime = time.time()
print(f'{round(elapsedTime - initialTime, 2)}s - {generatedImgs}/{totalImgs} -',
      f'{round(percentageConcluded)}%')
print(f'Conclusion time: {round(conclusionTime - initialTime, 2)}s')
