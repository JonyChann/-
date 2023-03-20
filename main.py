from imageai.Detection import ObjectDetection
import os
import sys
import json

execution_path=os.getcwd()  

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

def img_dt(img_path): #融合imageAI的识别函数
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "model/yolov3.pt"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=img_path, minimum_percentage_probability=30)
    lst=[]
    num=[]
    objectList={}
    for object in detections:
        obj=[object['name']]
        if obj not in lst:
            #print(obj)
            lst.append(obj)
            num.append(1)
        elif obj in lst:
            num[lst.index(obj)]+=1
    for object in lst:
        i = lst.index(object)
        objectList[object[0]] = num[i]
        #print(object+':'+str(num[i]))
    return lst,num

#读取中英对照的外部json文件
lud=open('translate.json','r',encoding='utf-8')
dict=json.load(lud)
lud.close()

#读取指定目录下的jpg/jpeg/png图片文件
files=os.listdir(get_arg('-i'))
file_list=[]
for file in files:
    if file[-3:] in ['jpg','JPG','PNG','png']:
        file_list.append(file)

#result=img_dt("images/multiPeople.png",json_read('translate.json'))
for file in file_list:
    print(get_arg('-i')+'\\'+file)
    output=img_dt(get_arg('-i')+'\\'+file)
    for item in output[0]:
        no=output[0].index(item)
        print(dict[item[0]]+' : '+str(output[1][no]))
