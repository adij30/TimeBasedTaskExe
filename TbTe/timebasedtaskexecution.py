from datetime import datetime


class TimeBaseTaskExe:
    def __init__(self, tasktype, name, starttm, endtm):
        self.tasktype = tasktype
        self.name = name
        self.starttm = starttm
        self.endtm = endtm

    def timebased(self):
        print('Your Entered Input: ')
        print(TaskType, User, StartTime, EndTime)
        print('Output:')
        current_time = datetime.now().time()
        if self.starttm < current_time < self.endtm:
            return True
        elif self.starttm < self.endtm < current_time:
            return False
        elif current_time < self.starttm < self.endtm:
            return self.starttm

    def enhancedtimebased(self):
        current_time = datetime.now().time()
        current_day = datetime.now().weekday()
        current_day_name = datetime.today().strftime("%A")
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        print('Your Entered Input: ')
        print(TaskType, User, StartTime, EndTime, day1, day2)
        print('Output:')
        if current_day_name == day1 or current_day_name == day2:
            if self.starttm < current_time < self.endtm:
                return True
            elif self.starttm < self.endtm < current_time:
                if current_day_name == day1:
                    return '{} {}'.format(day2, self.starttm)
                if current_day_name == day2:
                    return '{} {}'.format(day1, self.starttm)
            elif current_time < self.starttm < self.endtm:
                if current_day_name == day1:
                    return '{} {}'.format(day1, self.starttm)
                if current_day_name == day2:
                    return '{} {}'.format(day2, self.starttm)
        else:
            d1 = day_name.index(day1)
            d2 = day_name.index(day2)
            l1 = [d1, d2]
            l1.sort()
            if l1[-1] < current_day:
                return '{} {}'.format(day_name[l1[0]], self.starttm)
            else:
                for i in l1:
                    if i > current_day:
                        return '{} {}'.format(day_name[i], self.starttm)

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)


while True:
    TaskType = input('Enter your Task Type(Email,Call,SMS):', )
    User = input('UserName:', )

    while True:
        StartTime = input('Enter a Start time in 24Hours format as HH:MM:SS :', )
        Start_Time = (datetime.strptime(StartTime, '%H:%M:%S').time())
        EndTime = input('Enter a End time in 24Hours format as HH:MM:SS : ')
        End_Time = (datetime.strptime(EndTime, '%H:%M:%S').time())
        if Start_Time > End_Time:
            print('StartTime must be lesser than EndTime,Enter Again')
        else:
            break

    timebase = TimeBaseTaskExe(TaskType, User, Start_Time, End_Time)
    print('T/t-TimeBased\nE/e-EnhancedTimeBased')
    option = input("Choose your option please T/t OR E/e:")
    if option == 'T' or option == 't':
        print(timebase.timebased())
        break
    elif option == 'E' or option == 'e':
        print('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        day1 = input('Enter 1st day for Session(must entered as shown):',)
        day2 = input('Enter 2nd day for Session(must entered as shown):',)
        print(timebase.enhancedtimebased())
        break
