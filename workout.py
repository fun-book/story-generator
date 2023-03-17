class rm_duplicates():

    def remove_duplicates(self, actions_lists):
        duplicates = set()
        actions_lists1=[]
        # this step list is converted to string so easily identified dupilicates and partial dupilicates
        for i in range(len(actions_lists)):
             list=' '.join(actions_lists[i])
             list=list.replace('-','')
             list=list.replace(': ','')
             list=list.replace(' ','')
             actions_lists1.append(list)
        unique_lists = []
        for i in range(len(actions_lists)):
            is_duplicate = False
            is_partial = False
            for j in range(len(actions_lists)):
                if actions_lists1[i] is actions_lists1[j]:
                    continue
                # find dupicates  and remove dupilicates
                if actions_lists1[i] == actions_lists1[j]:
                    is_duplicate = True
                    actions_lists1[i]='NULL'
                    actions_lists[i]='NULL'
                    break
                # find partial dupiliactes and remove dupilicates
                if actions_lists1[i]!='NULL':
                  if actions_lists1[i]  in actions_lists1[j]:
                    is_partial = True
                    actions_lists1[i]='NULL'
                    actions_lists[i]='NULL'
                    break
            # check the variable is not ddupicates and not partial
            if actions_lists[i] != 'NULL':
               unique_lists.append(actions_lists[i])
        return unique_lists