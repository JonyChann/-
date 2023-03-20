from imageai.Detection import ObjectDetection
import os
import sys
import json

execution_path=os.getcwd()

def json_read(filepath): #读取中英对照的外部json文件
    lud=open('translate.json','r',encoding='utf-8')
    dict=json.load(lud)
    lud.close()
    return dict

def get_arg(par):
    global filepath
    argc=len(sys.argv)
    argv=sys.argv
    value=''
    for arg in range(0,argc): 
        if argv[arg] == (par) :#接受传入文件的路径
            value=(argv[arg+1])
        #elif argv[arg] == '-l' 接受其它参数，暂时空置
    return value

def img_dt(img_path,lut): #融合imageAI的识别函数
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "model/yolov3.pt"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=img_path, minimum_percentage_probability=30)
    lst=[]
    num=[]
    objectList={}
    for object in detections:
        obj=lut[object['name']]
        if obj not in lst:
            #print(obj)
            lst.append(obj)
            num.append(1)
        elif obj in lst:
            num[lst.index(obj)]+=1
    for object in lst:
        i = lst.index(object)
        objectList[object]=num[i]
        #print(object+':'+str(num[i]))
    return lst,num

#result=img_dt("multiPeople.png",json_read('translate.json')) 本行用于测试
path=get_arg('')
files=os.listdir(path)
print(files[100])