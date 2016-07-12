#This module uses a recursively called function to loop through a list of items.
#Argument level will insert tab-stops when a nested loop is encountered.
#Provide boolean option for indentation and make the level optional
def loop_print(a_list,indent=False,level=0):
    for item in a_list:
        if isinstance(item,list):
            loop_print(item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(item)
            
            

