quiz=[
    {
        "Question":"What is capital of Pakistan?",
        "Options":["A) Karachi","B) Lahore","C) Islamabad","D) Quetta"],
        "answer":"C"
    },{
        "Question":"Which is national flower of Pakistan?",
        "Options":["A) Lilly","B) Jasmin","C) Tulip","D)Daisy"],
        "answer":"B"
    },
    {
        "Question":"Which is national game of Paistan?",
        "Options":["A) Cricket","B) vollyball","C) Badminton","D) Hockey"],
        "answer":"D"
    },
    {
        "Question":"Python is ?",
        "Options":["A) snake","B)Country","C)programming language","D)Car"],
        "answer":"C"
    },
    {
        "Question":"Waht is boiling point of water?",
        "Options":["A) 100\u00B0C ","B) 90\u00B0C","C) 80\u00B0C","D) 70\u00B0C"],
        "answer":"A"

    }
]
score=0
for i in quiz:
      print(i["Question"])
      for j in i["Options"]:
           print(j)
      user_input=input("Enter your answer(A/B/C/D)").upper()
      if user_input==i["answer"]:
          print("Correct---")
          score+=1
      else:
          print("Wrong! Correcr answer is ",i['answer'])
print("Quiz finished! Your score is",score,"out of",len(quiz))
