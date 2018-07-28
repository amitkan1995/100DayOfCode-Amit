# Hackerrank Nested List problem



if __name__ == '__main__':
    #create an empty list 
    students_marks =[]
        
    #loop through n number of range input
    for _ in range(int(input())):
        
        #store name of student in name variable
        name = input()
                
        #store float type score of student in score variable
        score = float(input())
                
        #add the above name and score of the student inside of the empty list you created
        students_marks.append([name, score])
                
    #store students unique scores using set() function in sorted form using sorted() function       inside of scores variable using list comprehension
    scores = sorted(set([student_mark[1] for student_mark in students_marks]))
        
    #store name of the second low scorer in sorted form using sorted() function with the below condition using list comprehension
    second_low_scorers = sorted([student_name[0] for student_name in students_marks if student_name[1] == scores[1]])
        
    #use for loop to display each sorted name of second low scorer from second_low_scorers list variable
    for name in second_low_scorers:
        
        #display name of second low scorer
        print (name) 