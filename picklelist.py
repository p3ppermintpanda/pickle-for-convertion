import pickle
import os
from ast import Global

    # pickletestmoment #


# -------------- task list -------------- #

# Values
# First Number - List Number
# Second Number - Value / Reward
# Status - 0 Open, 1 In Progress, 2 Closed

def taskFunction():

    taskList = [[1,10,1],[2,50,2],[3,25,0],[4,69,1]]

    #pickle
    pickle_out = open("taskList.pickle", "wb")
    pickle.dump(taskList, pickle_out)
    pickle_out.close()
    print("Finished","\n")


    #unpickle
    pickle_in = open("taskList.pickle", "rb")
    taskList = pickle.load(pickle_in)


    print(taskList,"\n")
    task = input("Please select a task ")
    task = int(task)
    print("Selected",taskList[task-1][0],"\n")

    if taskList[task-1][2] == 0:
        status = "Open"
    elif taskList[task-1][2] == 1:
        status = "In Progress"
    elif taskList[task-1][2] == 2:
        status = "Closed"

    print("---------------------")
    print(" Task selected:",taskList[task-1][0],"\n","Reward:",taskList[task-1][1],"\n","Status:",status)
    print("---------------------","\n")


    if status == "In Progress":
        taskPermission = input("Do you want to vote for completion of this task? [y/n] ")
        if taskPermission == "y":
            listLength = item_list_counter(taskList)
            callVoting = voting(listLength, token_wallet)
            if callVoting == "pass":
                taskList[task-1][2] = '2'
                print(taskList)





def voting (number_of_task, token_wallet_voting):
    postive_vote=0
    negitve_vote=0
    vote_test1="fail"
    if token_wallet_voting<=0:
        print("you cant vote")
        return
    if token_wallet_voting>=1:
        while vote_test1=="fail":
            vote_choice=input("Do you wish for this action to pass? [y/n] "  )
            if vote_choice=="y" or vote_choice=="n":
                vote_test1="pass"
            else:
                print("Please input y or n")

        if vote_choice=="y":
            postive_vote=postive_vote+token_wallet_voting
        else:
            negitve_vote=negitve_vote+token_wallet_voting
        if postive_vote>negitve_vote:
            vote_status="pass"
            
        else:
            vote_status="fail"
        return(vote_status)




# --------- function ----------- #

def item_list_counter(list_ilc):
    list_count=list(list_ilc)
   
    for i in range(0, len(list_count)):
  
        if i == (len(list_count)-1):
            last_number=i+1
            return(last_number)


def create_proposal():
    global proposal_creation
    proposal_creation = 'proposalsList.pickle'

    proposal_list = []

    # first time you run this, "Preposals.dat" won't exist
    #   so we need to check for its existence before we load 
    #   our "database"
    if os.path.exists(proposal_creation):
        # "with" statements are very handy for opening files. 
        with open(proposal_creation,'rb') as rfp: 
            proposal_list = pickle.load(rfp)
        # Notice that there's no "rfp.close()"
        #   ... the "with" clause calls close() automatically! 

    username = input("Please enter your user name:")
    user_proposal = input("Please enter your proposal:")

    new_proposal = username, user_proposal
    proposal_list.append(new_proposal)

    #pickle
    pickle_out = open("proposalsList.pickle", "wb")
    pickle.dump(proposal_creation, pickle_out)
    pickle_out.close()
    print("Finished","\n")


    #unpickle
    pickle_in = open("proposalsList.pickle", "rb")
    taskList = pickle.load(pickle_in)

    print(proposal_list)
    return




# ----------- variables ----------- #

token_wallet = 1000000000

# #Pickle setup(can't be a function)
# aplacentList = 'proposalsList.pickle'

# proposal_list = []

# # first time you run this, "Preposals.dat" won't exist
# #   so we need to check for its existence before we load 
# #   our "database"
# if os.path.exists(aplacentList):
#     # "with" statements are very handy for opening files. 
#     with open(aplacentList,'rb') as rfp: 
#         proposal_list = pickle.load(rfp)
#     # Notice that there's no "rfp.close()"
#     #   ... the "with" clause calls close() automatically! 

# # Now we "sync" our database
# with open(aplacentList,'wb') as wfp:
#     pickle.dump(proposal_list, wfp)
# # Re-load our database
# with open(aplacentList,'rb') as rfp:
#     proposal_list = pickle.load(rfp)

# # ----------- proposal list ----------- #
 
# # Values
# # WalletID (Username)
# # Proposal Title

# # proposalsList = [("Username1","Give employees more ice cream"),("Username2","Give employees more hot dogs")]

# # #pickle
# # pickle_out = open("proposalsList.pickle", "wb")
# # pickle.dump(proposalsList, pickle_out)
# # pickle_out.close()
# # print("Finished","\n")

# # #unpickle
# # pickle_in = open("proposalsList.pickle", "rb")
# # taskList = pickle.load(pickle_in)

# # print(proposalsList)





# -------------- selection -------------- #

# ask what the objective of user is
    #task list
    #voting
    #make a proposal
# take user to selection

selection = input("\n Please select a number \n 1) View tasks and vote \n 2) Make a Proposal \n")
if selection == "1":
    call_taskFunction = taskFunction()
if selection == "2":
    call_create_proposal = create_proposal()





# if selection == "2":
#     task_perform_filename = "task_perform.pickle"
#     task_perform = []
#     if os.path.exists(task_perform_filename):
#         with open(task_perform_filename,'rb') as rfp: 
#             task_perform = pickle.load(rfp)
#     with open(task_perform_filename,'wb') as wfp:
#         pickle.dump(task_perform, wfp)
#     with open(task_perform_filename,'rb') as rfp:
#         task_perform = pickle.load(rfp) 
#         print(task_perform)


