

class Helpers:

    @staticmethod
    def evaluate_query(query_sample :str ,*args):
        try:
            return query_sample.format(*args)
        except:
            return None

    @staticmethod
    def check_number_of_rows(data,expectedrowcount=0):
        return True if len(data) == expectedrowcount else False,len(data), \
               None if len(data) == expectedrowcount else data

    @staticmethod
    def check_all_records_correspond_dictionary(data, expecteddict: dict):
        result = [each for each in data.to_dict('split')['data'] if not (each[0] in expecteddict and each[1]==expecteddict[each[0]])]
        return True if len(result) == 0 else False,len(result), \
               None if len(result) == 0 else result