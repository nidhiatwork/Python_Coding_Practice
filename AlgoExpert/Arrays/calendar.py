def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    st=None
    if greaterThanOrEqual(dailyBounds1[0],dailyBounds2[0]):
        st=dailyBounds1[0]
    else:
        st=dailyBounds2[0]

    end=None
    if greaterThanOrEqual(dailyBounds1[1],dailyBounds2[1]):
        end=dailyBounds2[1]
    else:
        end=dailyBounds1[1] 
    
    ans=[]
    i,j=0,0
    eligible = getDuration(st, meetingDuration)
    while not greaterThanOrEqual(eligible[1], end, False):
        while i<len(calendar1) and greaterThanOrEqual(eligible[0],calendar1[i][1]):
            i+=1
        while j<len(calendar2) and greaterThanOrEqual(eligible[0],calendar2[j][1]):
            j+=1
        if not (intersects(eligible, calendar1, i) or intersects(eligible, calendar2, j)):
            if ans and ans[-1][1]==eligible[0]:
                last_value=ans.pop()
                eligible=[last_value[0], eligible[1]]
            ans.append(eligible)
        eligible = getDuration(eligible[1], meetingDuration)
    return ans
        
def getDuration(st, meetingDuration):
    meetingSlot=[]
    hr,minute=st.split(':')[0], st.split(':')[1]
    meetingSlot.append(st)
    end=None
    carry=0
    minute_sum = int(minute)+meetingDuration
    if minute_sum<59:
        if minute_sum<10:
            minute_sum="0"+str(minute_sum)
        meetingSlot.append(hr+":"+str(minute_sum))
    else:
        carry=minute_sum//60
        minute_sum=minute_sum%60
        if minute_sum<10:
            minute_sum="0"+str(minute_sum)
        hr_sum=int(hr)+carry
        if hr_sum<10:
            hr_sum="0"+str(hr_sum)
        meetingSlot.append(str(hr_sum)+":"+str(minute_sum))        
    return meetingSlot

def intersects(slot1, cal2, i):
    return i<len(cal2) and \
            ((greaterThanOrEqual(slot1[0], cal2[i][0]) and not greaterThanOrEqual(slot1[0], cal2[i][1])) \
            or \
            (greaterThanOrEqual(slot1[1], cal2[i][0], False) and not greaterThanOrEqual(slot1[1], cal2[i][1])))

def greaterThanOrEqual(time1, time2, orEqual=True):
    time1_split = time1.split(":")
    time2_split = time2.split(":")
    hr1,hr2=time1_split[0], time2_split[0]
    min1,min2=time1_split[1], time2_split[1]    
    if int(hr1)>int(hr2):
        return True
    elif int(hr1)<int(hr2):
        return False
    else:
        if int(min1)>int(min2):
            return True
        elif int(min1)<int(min2):
            return False
        else:
            return orEqual

calendar1 = [
    ["9:00", "10:30"],
    ["12:00", "13:00"],
    ["16:00", "18:00"]
  ]

calendar2= [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"]
  ]
dailyBounds1= ["9:00", "20:00"]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 45

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))