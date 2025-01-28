import sympy

def gbdf(feature_lis,values,c_list,critical):
    #lists for features and critical values by order
    
    critical_ans = []
    not_critical_ans = []
    '''
    #c_n2 = 114.2
    #c_N1 = 350
    print ("You must enter at least 2 values: number of unique operands,total number of operators(each of them is a critical feature).Enter in this order.")
    x = float(input("Enter the number of unique operands in your code: "))
    critical.append(x > c_n2)
    x = float(input("Enter the total number of operators in your code: "))
    critical.append(x > c_N1)
    '''
    print("Based on the model, we have 8 features, each of which can be critical or not.") 
    print("If you would like to add another features? if so enter number of features.")
    features = int(input("How many more features do you have in your code?  "))
    #j=0

    for i in range(features):
        '''while j < len(c_list):
            # features from model
            if i+j < len(c_list):
                #we are in the 6 first feature user want to enter that may not be from model
                ans = input("Do you want to add feature '{}' for yes, enter 'Y': ".format(feature_lis[i + j] ))
                if ans == 'y' or ans == "Y" or ans == "yes":
                    value = float(input("Enter the value of the feature '{}':".format(feature_lis[i + j])))
                    answer = input("Is this feature critical? (T for True, F for False): ").strip().upper()
                    if answer == "F":
                        not_critical.append(value > c_list[i+j])
                    else:
                        critical.append(value > c_list[i+j])
                else:
                    #user wont add the feature
                    j += 1
        
        if i+j >= len(c_list):'''
        #user enter feature outside from model
        Value = float(input("Enter the value of the feature: "))
        C = float(input("Enter the critical value of the feature: "))
        answer = input("Is this feature critical? (T for True, F for False): ").strip().upper()
        feature_name = input("Enter the name of the feature: ")
        values.append(Value)
        c_list.append(C)
        feature_lis.append(feature_name)
        if answer == "F":
            critical.append('n')
            #not_critical.append(value > C)
        else:
            critical.append('y')
            #critical.append(value > C)
    
    print("Feature list:")
    print("\t" + ", ".join(feature_lis))
    print("\nC List (corresponding values):")
    print("\t" + ", ".join([f"{c:.2f}" for c in c_list]))
    print("\nValues:")
    print("\t" + ", ".join([f"{v:.5f}" for v in values]))
    print("Is it critical or not list:")
    print("\t" + ", ".join(critical))
    
    for value, c, crit in zip(values, c_list, critical):
        result = value > c  # Test if value > c
        if crit == 'y':
            critical_ans.append(result)
        elif crit == 'n':
            not_critical_ans.append(result)
    #boolian list status
    print("the critical boolian answers are:" + ", ".join(map(str, critical_ans)))
    print("the not critical boolian answers are:" + ", ".join(map(str, not_critical_ans)))
    #chacking
    if  len(not_critical_ans) == 0:
        return sum(critical_ans)
    else:
        return sum(not_critical_ans) == len(not_critical_ans) or  sum(critical_ans)
    




feature_lis = ["number of unique operands","total number of operators ","total number of operands ","exectable line of code", "number of unique operators" , "line of code","McCabe cyclomatic complexity", "number of ligical operators"]
c_list = [114.2, 350,311.36 , 59.36, 26.68, 841.96, 13.26, 1.16]
values1 = [0.1950,0.22587,1.9505,13.9025,0.022587,74.824,14.05308,2]
values2 = [0.1950,0.22587,1.9505,13.9025,0.022587,37.412,14.05308,2]
values3 = [0.1950,0.22587,1.9505,13.9025,0.022587,127.2008,14.05308,2]
critical = ['y','y','y','y','y','y','y','y']
code_stat =  gbdf(feature_lis,values3,c_list,critical)
if code_stat:
    print("Your code is not good.")
else:
    print("Your code is good.")