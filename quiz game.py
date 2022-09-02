import requests
import json
import random
import pprint
import html
accurate_answer=0
wrong_answer=0
url="https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple"#api link
game=""#variable empty string
while game !="quit":#while loop
    r=requests.get(url)
    if (r.status_code!=200):
        game=input("therir was a problem on retreving the question " "please enter to retry or press quit to exit the game")
    else:
        valid_answer=False
        answers_number=1
        data=json.loads(r.text)
        question=data['results'][0]['question']
        answers=data['results'][0]['incorrect_answers']
        correct_answer=data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        
        print(html.unescape(question))
        print("")


        for answer in answers:
            print(str(answers_number)+ "-" + html.unescape(answer))
            answers_number+=1
        while valid_answer==False:
            game_answer=input("type the number of the answer ")
            try:
                game_answer = int(game_answer)
                if game_answer > len(answers) or game_answer <= 0:
                    print("Invalid Answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Use only numbers.")
            
            game_answer=answers[int(game_answer)-1]
        if game_answer==correct_answer:
            print("your answer is correct ")   
            accurate_answer+=1
        else:
            print("you're wrong")  
            wrong_answer+=1
            print("##########################")
        print("correct answer is = ", accurate_answer)       
        print("wrong answer is = ",wrong_answer)       
        print("##########################")
      
        game=input("press enter to continue or type 'quit' to exit ")       
print("thankyou for playing")