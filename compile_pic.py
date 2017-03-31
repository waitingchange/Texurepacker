#!/usr/bin/python    
#encoding=utf-8    
# 脚本目的是通过执行脚本达到直接将每一个文件夹内部的资源打成大图 png plist 
# 要求，每个文件夹内部的图片资源不能超过  2048 * 2048 超过会报错
# 


import io  
import os  
import sys    
import hashlib    
import string    
import re  
  
  

UnpackFolderName = 'unpack_images'
  
ImageDir = './textures/'
OutputDirPNG = './cocosstudio/images/'

projectImageDir = '../res/images/'

  
print("ImageDir = " + ImageDir)  
print("OutputDirPNG = " + OutputDirPNG)  


def createPath(cPath):  
    if not os.path.isdir(cPath):  
        os.mkdir(cPath)  
  
def pack_action(inputPath, outputPath, opt, scale, maxSize, sheetSuffix, textureFormat, sizeConstraints, sheetName, otherParams, fileNameSuffix):  
    packCommand = "TexturePacker" + \
        " --format cocos2d" \
        " --maxrects-heuristics best" \
        " --enable-rotation" \
        " --shape-padding 2" \
        " --border-padding 0" \
        " --trim-mode Trim" \
        " --basic-sort-by Name" \
        " --basic-order Ascending" \
        " --texture-format {textureFormat}" \
        " --data {outputSheetNamePath}{fileNameSuffix}.plist" \
        " --sheet {outputSheetNamePath}{fileNameSuffix}.{sheetSuffix}" \
        " --scale {scale}" \
        " --max-size {maxSize}" \
        " --opt {opt}" \
        " --size-constraints {sizeConstraints}" \
        " {inputPath}" \
        " {otherParams}"  
  
  
    packCommand = packCommand.format(  
        textureFormat=textureFormat,  
        outputSheetNamePath=os.path.join(outputPath,sheetName),  
        sheetName=sheetName,  
        sheetSuffix=sheetSuffix,  
        scale=scale,  
        maxSize=maxSize,  
        opt=opt,  
        sizeConstraints=sizeConstraints,  
        inputPath=inputPath,  
        otherParams=otherParams,  
        fileNameSuffix=fileNameSuffix) 

    os.system(packCommand)  
  
if __name__ == '__main__':  
    createPath(OutputDirPNG)  
    for sheet in os.listdir(ImageDir):
        newDir = os.path.join(ImageDir, sheet)
        if os.path.isdir(newDir) and str(sheet) != UnpackFolderName:
            pack_action(newDir,OutputDirPNG,'RGBA8888',1,2048,'png',"png","AnySize",sheet,"--png-opt-level 7", "")


    moveCmd = 'cp -R ' + OutputDirPNG + '/ ' + projectImageDir
    os.system(moveCmd)

    # 删除 。dir 结尾的文件夹
    for sheet in os.listdir(projectImageDir):
        newDir = os.path.join(projectImageDir, sheet)
        if sheet.endswith(".Dir"):
            rmCmd = 'rm -rf ' + str(newDir)
            os.system(rmCmd)


    print 'packImag and move res complete..'


