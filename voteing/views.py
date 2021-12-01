
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from voteing.models import Voters
from voteing.models import constituency,add_election as addelection
import cv2
import os
import numpy as np
import face_recognition
from datetime import datetime
from PIL import Image

def index(request):

    return render(request , 'voteing/index.html')

def adminnx(request):

    return render(request , 'index1.html')


def add_election(request):
    error=""
    if request.method == "POST":

        etype= request.POST['election']
        start = request.POST['start']
        end = request.POST['end']
        rul = request.POST['rules']
   
        print(etype , start,end,rul)     
        elec=addelection(electiontype=etype,startdate=start,enddate=end,electionrules=rul)
        elec.save()
      
    print(error)    
    d={'data':error}
    return render(request ,'adminx/addelection.html' ,d)


def add_party(request):
    return render(request ,'adminx/addpartyinfo.html')


def add_Candidate(request):
    return render(request , 'adminx/candidate.html')


def add_Seat(request):
    return render(request ,'admin/addseat.html')



def about_ECP(request):
    return render(request , 'voteing/about.html')


def about_Elections(request):
    return render(request , 'voteing/elections.html')


def about_Parties(request):
    return render(request , 'voteing/parties&can.html')



def about_Updates(request):
    return render(request , 'voteing/latestupdate.html')


def Downloads(request):
    return render(request , 'voteing/downloads.html')


def contact_Us(request):
    return render(request , 'voteing/contactus.html')


def voter_Registration(request):
    return render(request , 'voteing/registration.html')


def voter_reg_form(request):
    error=""
    if request.method == "POST":


        resident= request.POST['resident']

        rights = request.POST['rights']
        conv = request.POST['convienced']
        oldd = request.POST['old']


        name = request.POST['name']
        dob= request.POST['dob']
        cni= request.POST['cnic']
        cons=request.POST['const']
        image = request.FILES['photox'] 
     
    
        try:
            try:
                user = User.objects.create_user(username=name, email="", password="")
            except:
                error="usernamealredyexist"
                return redirect({'error':error})
            voter=Voters(user=user ,cnic=cni,constituency=cons,dob=dob,image=image)
            voter.save()
            # pathh="C:\Users\Shahid\Desktop\vote\ECP\uploads"
        except:
            error="usernamealredyexist"
            pass
 
    data={'error':error}
    print(data)
    return render(request , 'voteing/voterregistration.html',data )
    # dic = {'error': error}
    # return render(request, 'job/user-register.html', dic)
    

def cast_Vote(request):
    return render(request ,'voteing/castvote.html')


def capture(request):
    return render(request,'voteing/capture.html')



def camera_Open(request):
    path = 'C:/Users/Shahid/Desktop/vote/ECP/uploads'
    images = []
    personNames = []
    myList = os.listdir(path)
    print(myList)
    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    print(personNames)
    encodeListKnown = faceEncodings(images)
    print('All Encodings Complete!!!')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
             # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personNames[matchIndex].upper()
            # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                attendance(name)

            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    cap.release()
    cv2.destroyAllWindows()
    


def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



def attendance(name):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tStr},{dStr}')
  






def show_Instructions(request):
    return render(request ,'voteing/instructions.html')
