
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from voteing.models import ELECTION_TYPE, Voters,symbol,seat,Candidate,Parties,news
from voteing.models import constituency,add_election as addelection,leader,ElectionReslts
import cv2
import os
import numpy as np
import face_recognition
from datetime import datetime
from PIL import Image
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as log, logout, login

def index(request):

    return render(request , 'voteing/index.html')

def adminnx(request):
    if request.method=="POST":
        email=request.POST['email']
        passd=request.POST['password1']
        user = authenticate(request, username=email, password=passd)
        if user is not None:
           

            try:
                # user12 = User.objects.get(user=user)

                if user.is_staff:
                    login(request, user)
                    messages.success(request , 'Login Successfully')
                    return redirect('admindash')
                    print('//////////')
                    print("login")
                    error = "no"
                else:
                    messages.success(request , 'User in not Staff user')
                    return redirect('aadmin')
            except:
                messages.error(request ,'not staff')

        else:
            messages.error(request , 'User not found')


    return render(request , 'adminx/login.html')
    # return render(request , 'index1.html')


def adminlogout(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('/admin')
    else:
        logout(request)

        return redirect('/')



def admin_Dash(request):
    
    return render(request , 'index1.html')

def add_election(request):
    error=""
    if request.method == "POST":

        etype= request.POST['election']
        start = request.POST['start']
        end = request.POST['end']
        rul = request.POST['rules']
   
        try:  
            elec=addelection(electiontype=etype,startdate=start,enddate=end,electionrules=rul)
            elec.save()
            messages.success(request , 'Election added successfully')
            return redirect('addelection')
        except:
            messages.error(request ,"there is something wrong in addeing election")
            return redirect('addelection')  
    d={'data':error}
    return render(request ,'adminx/addelection.html' ,d)


def add_party(request):
    error=""
    x=leader.objects.all()
    sym=symbol.objects.all()
    if request.method=="POST":
        pname=request.POST['name']
        plead=request.POST['leader']
        ps=request.POST['symb']
        pover=request.POST['partyover']
        
        pleadx=leader.objects.get(leaderName=plead)
        psym=symbol.objects.get(symbolName=ps)
        try:

            pat=Parties(partyName=pname,partyLeader=pleadx ,partySymbol=psym ,partyOverview=pover)
            pat.save()
            messages.success(request, 'Party added successfully.')
        except:
            messages.error(request, 'something wrong in saveing record.') 
        return redirect('addparty')
    
 
    d={'data':x,'symbol':sym}
    
    return render(request ,'adminx/addpartyinfo.html',d)


def addpartyleader(request):
    if request.method=="POST":
        leadnam=request.POST['lname']
        try:
            led=leader(leaderName=leadnam)
            led.save()
            messages.success(request , 'Leader added successfully')
            return redirect('addpartyleader')
        except:
            messages.error(request ,'maybe leader name is already exist (Please try with other name)')
            return redirect('addpartyleader')
        
    return render(request , 'adminx/partyleader.html')

def addpartysymbol(request):

    if request.method=="POST":
        synam=request.POST['sname']
        simg=request.FILES['simgx']
        try:
            sy=symbol(symbolName=synam ,symbolImage=simg)
            sy.save()
            messages.success(request , 'Symbol added successfully')
            return redirect('addpartysymbol')
        except:
            messages.error(request ,'maybe symbol name is already exist (Please try with other name)')
            return redirect('addpartysymbol')

    
    return render(request , 'adminx/partysymbol.html')


def add_Candidate(request):
    da=Parties.objects.values_list('partyName',flat=True)
    sym=symbol.objects.values_list('symbolName',flat=True)
    se=seat.objects.values_list('seatName',flat=True)
    elec=addelection.objects.all()
    if request.method=="POST":
        pnam=request.POST['partyn']
        psymb=request.POST['psym']
        pseat=request.POST['psea']
        cname=request.POST['cnam']
        celec=request.POST['elec']
        img=request.FILES['imgx']
        
        try:
            try:
                usr=User.objects.create(username=cname , email="" , password="")
            except:
                pass
            prty=Parties.objects.get(partyName=pnam)
            syy=symbol.objects.get(symbolName=psymb)
            se=seat.objects.get(seatName=pseat)
            elec=addelection.objects.get(electiontype=celec)
            
            can=Candidate(user=usr , party=prty,election=elec,seat=se,image=img)
            can.save()
            messages.success(request , "Candidate added successfully")
            return redirect('addcandidate')
        except:
            messages.error(request , "Maybe candidate is already added")
            return redirect('addcandidate')
            
    
    d={'pn':da, 'snam':sym,'seat':se,'election':elec}
    return render(request , 'adminx/candidate.html',d)


def add_Seat(request):
    sea=seat.objects.all()
    # can=Candidate.objects.all()
    # par=Parties.objects.all()
    # d={'seat':sea,'candidate':can,'parties':par}
    if request.method=="POST":
        snam=request.POST['sename']
        try:
            sn=seat(seatName=snam)
            sn.save()
            messages.success(request , 'Seat added successfully')
            return redirect('addseat')
        except:
            messages.error(request , 'maybe this seat is already exists')
            return redirect('addseat')
    return render(request ,'adminx/addseat.html')



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

    se=seat.objects.all() 
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
 
    data={'error':error , 'seat':se}
    print(data)
    return render(request , 'voteing/voterregistration.html',data )
    # dic = {'error': error}
    # return render(request, 'job/user-register.html', dic)
    

def cast_Vote(request):
    return render(request ,'voteing/castvote.html')


def capture(request ,id):
    vid=request.user.id
    cascan = id
    
    d={'candidate':cascan , 'voter':vid}
    return render(request,'voteing/capture.html' , d)



def camera_Open(request):
    cnic=""
    cid=""
    if request.method=="POST":
        try:
            cnic=request.POST['cnic']
            usr=Voters.objects.get(cnic = cnic)
        except:
            return redirect('reg_form')


    else:
        return redirect("/home")
    if cnic:
        pass
    else:
        return redirect('/home')    
    
    print("////////////////")
    print(cid)

    print(cnic)
    
    path = 'C:/Users/Shahid/Desktop/vote/ECP/uploads/voter/'
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
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
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
                name = personNames[matchIndex]
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
               
                
                # userx = User.objects.get(id=request.user.id)
                
               
                usr=Voters.objects.get(cnic = cnic)
              
               
               
                cuser=User.objects.get(id=cid)
             
                userr=User.objects.values_list('username', flat=True).get(username=usr)
               
                caa=Candidate.objects.get(user = cuser)
                print("///////")
                # print(userr)
                # print(type(cuser))
                # print(userr)
                # print(caa.party)
                # print(caa.seat)
                
               
                # par=Parties.objects.get(partyName = caa.party)
                # sea=seat.objects.get(seatName=caa.seat)
                # print(usr)
                # print(caa.cuser)
                par=caa.party
                sea=caa.seat
                
                if userr==name:

                    try:
                        ex=ElectionReslts(vuser=userr , Candidate=cuser , party=par , seat=sea)
                        ex.save()
                        messages.success(request , 'Vote Casted Successfully')
                        destroy(cap)
                        return redirect('/')
                    except:

                        messages.error(request , 'Maybe You already Cast Your Vote')
                        destroy(cap)
                        return redirect('/')

                else:
                    print(userr)
                    print(name)

                
                
            else:
               
                destroy(cap)
                return redirect('reg_form')
                break

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()


def destroy(cap):
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
  


def ballet(request):
    can=Candidate.objects.all()

    print('////////////////////')
    d={'cand':can}
    return render(request , 'voteing/ballet.html' , d)


def addNews(request):
    if request.method == "POST":

        tit= request.POST['tit']

        content = request.POST['cont']
             
        image = request.FILES['img'] 
     
    
        try:
            try:
                
                user = User.objects.get(username= request.user)
            except:
                
                messages.error(request , "error in fetch user")
                return redirect('/admindash')
            voter=news(author=user ,title=tit,content=content,image=image)
            voter.save()
            messages.success(request ,'news added successfully ')
            return redirect('/news')
            # pathh="C:\Users\Shahid\Desktop\vote\ECP\uploads"
        except:
            messages.error(request ,'error in saveing news')
            return redirect('/news')

    return render(request , 'adminx/addnews.html')



def show_Instructions(request):
    return render(request ,'voteing/instructions.html')





# //admin

def check_voter_reg(request):
    return render(request , 'adminx/checkreg.html')


def results(request):
    return render(request , 'adminx/showresult.html')




def honourable__ecp(request):
    return render(request , 'voteing/honourecp.html')



def electionResult(request):
    
    return redirect('/castvote')



def checkCnic(request , cid):
    d={'cid':cid}
    return render(request , 'voteing/cniccheck.html' , d) 


def partiesList(request):
    parties=Parties.objects.all()

    d={'partiesx':parties}
    return render(request , 'voteing/listofparties.html', d)


def symbolList(request):


    sym=symbol.objects.all()

    d={'symbol':sym}
    return render(request , 'voteing/listofsymbol.html', d)


def candidateList(request):


    sym=Candidate.objects.all()

    d={'candidate':sym}
    return render(request , 'voteing/listofcandidate.html', d)

def checkRegestration(request):
    if request.method=="POST":
        cnic = request.POST['cnic']
        try:
            vot=Voters.objects.get(cnic=cnic)
        except:
            vot=""    
        if vot:
            messages.success(request , 'Your Are Register For Voteing')
            return redirect('ckeckreg')
        else:

            messages.error(request , 'Your Are Not Register For Voteing')
            return redirect('ckeckreg')

    return render(request , 'voteing/checkreg.html')


    return render(request, 'job/user-register.html', dic)

# @login_required(login_url='/login')
# def adminlogin(request):
    

#     return render(request, 'adminx/login.html', dic)

