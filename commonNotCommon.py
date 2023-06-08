def commonNotCommon(new_Mainstream,new_must_watch):
    common_arr=[]
    for i in new_Mainstream:
        if i in new_must_watch:
            common_arr.append(i)
            new_Mainstream.remove(i)
            new_must_watch.remove(i)
    uncommon_arr=new_Mainstream+new_must_watch
    final_arr=[]
    final_arr.append(common_arr)
    final_arr.append(uncommon_arr)
    #final_arr = np.array([common_arr,uncommon_arr])
    return final_arr

    

Mainstream = [x for x in input().split()]
must_watch = [x for x in input().split()]
new_Mainstream = [*set(Mainstream)] 
new_must_watch = [*set(must_watch)]
answer=commonNotCommon(new_Mainstream,new_must_watch)
print(answer)