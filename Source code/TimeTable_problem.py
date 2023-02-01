import random
import prettytable


Population_Size = 9

NUMB_OF_ELITE_SCHEDULES = 1

TOURNAMENT_SELECTION_SIZE = 3

MUTATION_RATE = 0.1

class Database:
     numofinstructors = [["I1" , "DR mohamed"], ["I2" , "Dr ahmed "],["I3" , "Dr aya"],["I4" , "Dr tabark"]]
     meetings = [["MT1", "MWF 08:30 - 09:30 AM"], ["MT2", "MWF 09:30 - 10:30"],
                ["MT3", "TTH 08:30 - 10:00 A"],  ["MT4", "TTH 10:00 - 11:30"]]
     numofrooms = [["R1", 25], ["R2", 45], ["R3", 35]] 
     def __init__ (self) :
         self._Instructors = [] 
         self._Meetingtime = []          
         self._Rooms = []
         for n in range(0, len(self.numofinstructors)):
             self._Instructors.append(Instructor(self.numofinstructors[n][0], self.numofinstructors[n][1])) 
         for n in range(0, len(self.meetings)):
             self._Meetingtime.append(meetingtime(self.meetings[n][0], self. meetings[n][1]))           
         for n in range(0, len(self.numofrooms)):
             self._Rooms.append(Room(self.numofrooms[n][0], self.numofrooms[n][1]))
         c3 = Course("C3", "Cs361", [self._Instructors[3]], 35)
         c1 = Course("C1", "Cs352", [self._Instructors[0], self._Instructors[1], self._Instructors[2]], 35)
         c2 = Course("C2", "is313", [self._Instructors[2], self._Instructors[3]], 30)
         depart1 = Department("cs", [c1, c3])
         depart2 = Department("is", [c2 ])
         self._departs = [depart1, depart2]
         self._numOfclasses = 0
         for n in range(0, len(self._departs)): 
             self._numOfclasses += len(self._departs[n].get_ListOfCourses())  
         
         self._courses = [c1, c2, c3]
     def getnumofinstructors(self):   return self._Instructors
     def getMeetingtime(self):        return self._Meetingtime
     def getnumofrooms(self):         return self._Rooms
     def getdeparts(self):            return self._departs
     def getnumofcourses(self):       return self._courses
     def getnumOfclasses(self):       return self._numOfclasses    

class schedule:
    def __init__(self):
        self._classes = []
        self._fitness = -1
        self._no_conflicts = 0
        self._class_num = 0
        self._isfitnesschanged = True
        
    def intialize_class(self):
        Depts = data.getdeparts()
        for i in range(0, len(Depts)):
            course = Depts[i].get_ListOfCourses()
            for j in range(0, len(course)):
                class2 = Class(self._class_num, Depts[i], course[j]) 
                self._class_num += 1
                class2.set_instructor(course[j].get_Instructor_Name()[random.randrange(0, len(course[j].get_Instructor_Name()))]) 
                class2.set_room(data.getnumofrooms()[random.randrange(0,len(data.getnumofrooms()))]) 
                class2.set_meetingtime(data.getMeetingtime()[random.randrange(0, len(data.getMeetingtime()))])
                self._classes.append(class2)
        return self

    def get_class(self):
        self._isfitnesschanged = True
        return self._classes

    def calc_fitness(self):
        classes = self.get_class()
        self._no_conflicts = 0
        for i in range(0, len(classes)):
            if classes[i].get_room().get_Capacity() < classes[i].get_course().get_Students_Num():
                self._no_conflicts += 1
            for j in range(i + 1, len(classes)):
                if(classes[j].get_meetingtime() == classes[i].get_meetingtime()):
                    if(classes[j].get_room() == classes[i].get_room()):
                        self._no_conflicts += 1
                    if(classes[j].get_instructor() == classes[i].get_instructor()):
                        self._no_conflicts += 1
        return 1/(1.0 * self._no_conflicts+1)

    def get_no_of_conflict(self):
        return self._no_conflicts

    def get_fitness(self):
        if self._isfitnesschanged == True:
            self._isfitnesschanged = False
            self._fitness = self.calc_fitness()
        return self._fitness

    def __str__(self):
        String = ""
        for i in range(0,len(self._classes)):
            String+= str(self._classes[i])+" , "
        String += str(self._classes[len(self._classes)-1])
        return String


class Department:
    def __init__(self, department_name, ListOfCourses):
        self._Depart_Name = department_name
        self._Depart_Courses = ListOfCourses

    def get_department_name(self): return self._Depart_Name

    def get_ListOfCourses(self): return self._Depart_Courses


class Instructor:
    def __init__(self, instructor_id, instructor_name):
        self._Instructor_ID = instructor_id
        self._Instructor_Name = instructor_name

    def get_Instructor_id(self): return self._Instructor_ID 

    def get_Instructor_name(self): return self._Instructor_Name


class Course:
    def __init__(self, course_num, course_name, instructor_name, students_num):
        self._Course_Num = course_num
        self._Course_Name = course_name
        self._Instructor_Name = instructor_name
        self._Students_Num = students_num
  
    def get_Course_Num(self): return self._Course_Num
  
    def get_Course_Name(self): return self._Course_Name
  
    def get_Instructor_Name(self): return self._Instructor_Name
  
    def get_Students_Num(self): return self._Students_Num


class Room:
    def __init__(self, room_num, seating_num):
        self._Room_Num = room_num
        self._Seating_Num = seating_num

    def get_room_num(self):return self._Room_Num

    def get_Capacity(self): return self._Seating_Num

    # def __str__ (self): return f"{self.get_room_num()} ({self.get_Capacity()})"


class meetingtime:
    def __init__(self, id, time):
        self._ID = id
        self._Time = time

    def get_id(self): return self._ID

    def get_time(self): return self._Time


class Genetic_Algo :
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_scheduleds().append(pop.get_scheduleds()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < Population_Size:
            schedule1 = self._select_tournament_population(pop).get_scheduleds()[0]
            schedule2 = self._select_tournament_population(pop).get_scheduleds()[0]
            crossover_pop.get_scheduleds().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop
    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, Population_Size):
            self._mutate_schedule(population.get_scheduleds()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = schedule().intialize_class()
        for i in range(0, len(crossoverSchedule.get_class())):
            if (random.random() > 0.5):
                crossoverSchedule.get_class()[i] = schedule1.get_class()[i]
            else:
                crossoverSchedule.get_class()[i] = schedule2.get_class()[i]
        return crossoverSchedule


    def _mutate_schedule(self,mutateSchedule):
        schedule1 = schedule().intialize_class()
        for i in range(0, len(mutateSchedule.get_class())):
            if(MUTATION_RATE > random.random()):
                mutateSchedule.get_class()[i] = schedule1.get_class()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_scheduleds().append(pop.get_scheduleds()[random.randrange(0, Population_Size)])
            i += 1
        tournament_pop.get_scheduleds().sort(key=lambda x:x.get_fitness(), reverse=True)
        return tournament_pop


class Class:
    def __init__(self, num, dept, course):
        self._Num =num
        self._deprt = dept
        self._course = course
        self._meeting_time = None
        self._room = None
        self._instructor = None


    def get_Class_Num(self):
        return self._Num

    def get_dept(self):
        return self._deprt

    def get_course(self):
        return self._course  

    def set_meetingtime(self, new_meeting):
        self._meeting_time = new_meeting

    def get_meetingtime(self):
        return self._meeting_time

    def set_room(self, new_room):
        self._room = new_room    

    def get_room(self):
        return self._room

    def set_instructor(self, new_instructor):
        self._instructor = new_instructor  

    def get_instructor(self):
        return self._instructor  

    def __str__(self):
        return str(self._deprt.get_department_name()) + "," + str(self._course.get_Course_Name()) + "," + \
               str(self._room.get_room_num()) + "," + str(self._instructor.get_Instructor_id()) + "," + str(self._meeting_time.get_id())


class Population:
    def __init__(self, size):
        self._size = size
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(schedule().intialize_class())
 
    def get_scheduleds(self):
        return self._schedules  


class Printing:
    def print_class (self ,Schedule):
        Class = Schedule.get_class()
        table1 = prettytable.PrettyTable(["Class Num" , "Dept" , "Course(Number,Students_Num)","Room(Capacity)","Instructor(ID)","MeetingTime(MettingID)"])
        for i in range(0,len(Class)):
            table1.add_row([str(i), Class[i].get_dept().get_department_name(), 
            Class[i].get_course().get_Course_Name() + "(" + Class[i].get_course().get_Course_Num() + "," + str(Class[i].get_course().get_Students_Num()) + ")",
            Class[i].get_room().get_room_num() + "(" + str(Class[i].get_room().get_Capacity()) + ")",
            Class[i].get_instructor().get_Instructor_name() + "(" + str(Class[i].get_instructor().get_Instructor_id()) + ")",
            Class[i].get_meetingtime().get_time() + "(" + str(Class[i].get_meetingtime().get_id()) + ")"])
        print(table1)
    def print_schedule(self , populations):
        table2 = prettytable.PrettyTable(["Schedule_Num","Fitness","No_Of_Conflicts","Class(Dept,Course_Num,Room_Num,Instructor_ID,Meeting_ID)" ])
        schedules = populations.get_scheduleds()
        for j in range(0 , len(schedules)):
             table2.add_row([str(j),round(schedules[j].get_fitness(),3),schedules[j].get_no_of_conflict(),schedules[j]])
        print(table2)

data = Database()
display = Printing()
generation_num = 0
print("Generation "+str(generation_num))
population = Population(Population_Size)
population.get_scheduleds().sort(key=lambda x : x.get_fitness() , reverse=True )
display.print_schedule(population)
display.print_class(population.get_scheduleds()[0])
genetic_algo = Genetic_Algo()
while(population.get_scheduleds()[0].get_fitness()!=1.0):
    generation_num += 1
    print("Generation " + str(generation_num))
    population = genetic_algo.evolve(population)
    population.get_scheduleds().sort(key=lambda x: x.get_fitness() , reverse = True)
    display.print_schedule(population)
    display.print_class(population.get_scheduleds()[0])
print("\n\n")


