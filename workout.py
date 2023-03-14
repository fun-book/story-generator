class rm_duplicates():

    def remove_duplicates(self, actions_lists):
        duplicates = set()
        unique_lists = []
        for lst in actions_lists:
            is_duplicate = False
            is_partial = False
            for other_lst in actions_lists:
                if lst is other_lst:
                    continue
                if lst == other_lst:
                    is_duplicate = True
                    duplicates.add(tuple(lst))
                    break
                if all(elem in other_lst for elem in lst):
                    is_partial = True
                    duplicates.add(tuple(lst))
                    break
            if not is_duplicate and not is_partial:
             unique_lists.append(lst)
        unique_lists = [lst for lst in unique_lists if tuple(lst) not in duplicates]
        return unique_lists