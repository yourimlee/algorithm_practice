def solution(answers):
    
    s1=[1,2,3,4,5]
    s2=[2,1,2,3,2,4,2,5]
    s3=[3,3,1,1,2,2,4,4,5,5]
    
    ans_s1=0
    ans_s2=0
    ans_s3=0
    
    for i in range(len(answers)):
        if s1[i%len(s1)]==answers[i]:
            ans_s1+=1
       
        if s2[i%len(s2)]==answers[i]:
            ans_s2+=1
     
        if s3[i%len(s3)]==answers[i]:
            ans_s3+=1
    
    max_answer=max(ans_s1,ans_s2,ans_s3)
    ans=[]

    if max_answer==ans_s1:
        ans.append(1)
    if max_answer==ans_s2:
        ans.append(2)
    if max_answer==ans_s3:
        ans.append(3)
    return ans
