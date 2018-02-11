


class NotDivideError(Exception):
    pass

def divider_factory(divide_list):
    '''
    This function is floor-preferenced.
    :param divide_list: the intervals
    :return: the generated divider
    '''

    divide_list.append(10000)
    divide_list.insert(0, 0)
    def divider(data):
        for index in range(len(divide_list[0:-1])):
            if data > divide_list[index] and data <= divide_list[index+1]:
                ret = divide_list[index]
                return ret

        raise NotDivideError
    return divider


