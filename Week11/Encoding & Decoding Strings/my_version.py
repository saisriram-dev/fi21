def encode(strs):
    encoded_string = "23erty".join(strs)

    if strs == []:
        encoded_string = ""
    elif strs == [""]:
        encoded_string = '[""]'

    return encoded_string


def decode(s):
    decoded_strs = s.split("23erty")

    if s == "":
        decoded_strs = []
    elif s == '[""]':
        decoded_strs = [""]

    return decoded_strs
