import re


def case_punc(input_string):
    # Step-1: Non-ascii
    res = re.sub(r'[^\x00-\x7F]+',' ', input_string)

    # Step-2: URLs
    res = re.sub(r'http[s]?\:\/\/.[a-zA-Z0-9\.\/\_?=%&#\-\+!]+',' ', res)
    res = re.sub(r'pic.twitter.com?.[a-zA-Z0-9\.\/\_?=%&#\-\+!]+',' ', res)

    # Step-3: mentions
    # res = re.sub(r'\@([\w]+)',' ', res)
            
    # Step-4_alt-1: tagar
    # res = re.sub(r'\#([\w]+)',' ', res)
    # Step-4_alt-2: Word Spliting by Capitalize Case
    res = re.sub(r'((?<=[a-z])[A-Z]|[A-Z](?=[a-z]))', ' \\1', res)
    #res = re.sub(r'([A-Z])(?<=[a-z]\1|[A-Za-z]\1(?=[a-z]))',' \\1', res)
            
    # Step-5: Symbol
    res = re.sub(r'[!$%^&*@#()_+|~=`{}\[\]%\-:";\'<>?,.\/]', ' ', res)

    # Step-6: Number
    res = re.sub(r'[0-9]+','', res)

    # Step-7: Duplicate 3 Characters, convert to 1 Character
    res = re.sub(r'([a-zA-Z])\1\1','\\1', res)

    # Step-8: Multiple Space
    res = re.sub(' +', ' ', res)
            
    # Step-9: Space (First and Last)
    res = re.sub(r'^[ ]|[ ]$','', res)
            
    # Step-10: LowerSpace
    res = res.lower()
            
    return res
