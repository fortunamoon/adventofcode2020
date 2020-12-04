from day2_puzzle_data import puzzle_raw_data


def parse_data():
    # Sample Data format  '3-5 g: gggggg',
    valid_policies = 0
    for item in puzzle_raw_data:
        my_parse_s1 = item.split(":")
        my_parse_s2 = my_parse_s1[0].split(' ')
        temp_policy_s1 = my_parse_s2[0]
        temp_policy_s2 = temp_policy_s1.split("-")
        policy_begin = int(temp_policy_s2[0])
        policy_end = int(temp_policy_s2[1])
        temp_key = my_parse_s2[1]
        temp_password = my_parse_s1[1]
        if policy_begin <= temp_password.count(temp_key) <= policy_end:
            valid_policies+=1
    return valid_policies


if __name__ == '__main__':
    print(f'The total amount of valid policies is {parse_data()}')



