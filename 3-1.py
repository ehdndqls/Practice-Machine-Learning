from datetime import datetime


place=input("")
time=input("")
opponent=input("")
goals=input("")
aids=input("")
score_me=input("")
score_you=input("")


news="[프리미어 리그 속보("+str(datetime.now())+")]\n"
news=news+""+place+""+time+""
news=news+""+opponent+""

if score_me>score_you:
    news=news+""+score_me+""+score_you+""
elif score_me<score_you:
    news=news+""+score_me+""+score_you+""
else:
     news=news+""+score_me+""+score_you+""
     
if int(goals)>0 and int(aids)>0:
    news=news+""+goals+""+aids+""
elif int(goals)>0 and int(aids)==0:
    news=news+""+goals+""
elif int(goals)==0 and int(aids)>0:
    news=news+""+aids+""
else:
    news=news+""
    
    print(news)