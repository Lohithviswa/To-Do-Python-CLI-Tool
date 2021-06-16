import sys
from datetime import date

args = sys.argv
pending=0;completed=0


try:
    command = args[1]
except IndexError:
    print("Usage :-\n$ ./todo add \"todo item\"  #Add a new todo\n$ ./todo ls               #Show remaining todos\n$ ./todo del Number       #Delete a todo\n$ ./todo done Number      #Complete a todo\n$ ./todo help             #Show usage\n$ ./todo report          #Statistics")
    
    sys.exit(1)

if command not in ("add","del","done","help","report","ls"):
    print("Invalid command, Use add/del/done/help/report")

if command == "add":
    try:
       task = args[2]
    except:
       pass
    try:
       file = open("tasks.txt", "r")
    except IOError as e:
       print(str(e))
       sys.exit(1)
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    #print(tasks)
    if task not in tasks:
       file = open("tasks.txt", "a")
       file.write(task+"\n")
       file.close()
       print("Added todo: "+'\"'+task+'\"')
    
  
elif command == "del":
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)

    tasks = file.readlines()
    file.close()
    tasks = [task.strip() for task in tasks]
    try:
      index = args[2]
      index=int(index)-1
      del tasks[index]
      file = open("tasks.txt", "w")
      tasks = [task + "\n" for task in tasks]
      file.writelines(tasks)
      print("Deleted todo #{0}".format(index+1))
    except:
      print("Error: Missing NUMBER for deleting todo.")
    

elif command == "ls": 
    try:
       file = open("tasks.txt", "r")
    except IOError as e:
       print(str(e))
       sys.exit(1)

    tasks = file.readlines()
    i=len(tasks)
    if len(tasks) == 0:
        print("There are no pending todos!")
    else:
        
        tasks = [task.strip() for task in tasks]
       
        for j in range(len(tasks)-1,-1,-1) :
            print("[{0}] {1}".format(i,tasks[j]))
            i-=1
    file.close()  

elif command == "done":
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)

    tasks = file.readlines()
    file.close()
    tasks = [task.strip() for task in tasks]
    try:
      index = args[2]
      index=int(index)-1
    
      file = open("done_tasks.txt", "a")
      file.write(tasks[index]+"\n")
      file.close()
      
      del tasks[index]
      file = open("tasks.txt", "w")
      tasks = [task + "\n" for task in tasks]
      file.writelines(tasks)
      if int(index)+1==0:
           print("Error: todo #0 does not exist.")
      else:
           print("Marked todo #{0} as done.".format(int(index)+1))
    except:
      print("Error: Missing NUMBER for marking todo as done.")
    
    

    
    

elif command == "help":
    '''print("Usage :-")
    print('$ ./todo add "todo item"  #Add a new todo')
    print('$ ./todo ls               #Show remaining todos')
    print('$ ./todo del Number       #Delete a todo')
    print('$ ./todo done Number      #Complete a todo')
    print('$ ./todo help             #Show usage')
    print('$ ./todo report"          #Statistics')'''
    print("Usage :-\n$ ./todo add \"todo item\"  #Add a new todo\n$ ./todo ls               #Show remaining todos\n$ ./todo del Number       #Delete a todo\n$ ./todo done Number      #Complete a todo\n$ ./todo help             #Show usage\n$ ./todo report          #Statistics")
    
    
elif command == "report":
    today=date.today()

    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)

    tasks = file.readlines()
    file.close()
    tasks = [task.strip() for task in tasks]
    pending=len(tasks)
    try:
        file = open("done_tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)

    tasks = file.readlines()
    file.close()
    tasks = [task.strip() for task in tasks]
    tasks=list(set(tasks))
    completed=len(tasks)
    print(today,"Pending : {0} Completed : {1}".format(pending,completed)) 
    
else:
    print("invalid command!")
