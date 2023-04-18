#voting system using python

nominee_1=input("Donald Trump as 1 : ")
nominee_2=input("Joe Biden as 2: ")

nominee_1_votes=0
nominee_2_votes=0

votes_id=[1,2,3,4,5,6,7,8,9,10,11,12]
voters_number=len(votes_id)

while True:
    if votes_id==[]:
        print('Voting sessions is over')
        if nominee_1_votes>nominee_2_votes:
            percent=(nominee_1_votes/voters_number)*100
            print('Donald Trump has won with',percent,'% votes')
            break
        elif nominee_2_votes>nominee_1_votes:
            percent=(nominee_2_votes/voters_number)*100
            print('Joe Biden has won with',percent,'% votes')
            break

    else:
       voter=int(input("Enter your voter id no : "))
       if voter in votes_id:
          print("You are a voter :")
          votes_id.remove(voter)
          vote=int(input('Enter your vote 1 or 2: '))
          if vote==1:
            nominee_1_votes+=1
            print('Thank you for casting your vote:')

          elif vote:
            nominee_2_votes+=1
            print('Thank you for casting your vote:')
       else:
          print('You are not a voter here or you have voted already...')
