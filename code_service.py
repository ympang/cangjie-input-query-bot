import re
from sqlalchemy import create_engine
from sqlalchemy import select
from models import CodeInfo
from root_list import *
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)


def get_code(word):
    with engine.connect() as conn:
        select_stmt = select(CodeInfo).where(CodeInfo.word == word)
        result = conn.execute(select_stmt).fetchone()
    return result["code"]


def get_chi_code(eng_code):
    chi_code = [root["chi_root"] for root in root_list if root["eng_root"] == eng_code]
    return chi_code[0]


def get_chi_code_list(eng_code_list):
    chi_code_list = ""
    for eng_code in eng_code_list:
        chi_code_list += get_chi_code(eng_code)
    return chi_code_list


# result = []
# ipath = '下次咁@平123rrr順豐12到付。'
# # # print(len(ipath))
# new_path = re.findall(r'[\u4e00-\u9fff-\u3000-\u3003\u3008-\u300F\u3010-\u3011\u3014-\u3015\u301C-\u301E]+', ipath)
# # # print(new_path)
# word_list = []
# for word in new_path:
#     word_list.extend(list(word))

# result = [{**{'word': word, 'code':get_code(word), 'chi_code': get_chi_root_list(get_code(word))}} for word in word_list]
# print(result)
# print(word_list)
# code_list = [get_code(word) for word in word_list]
# print(code_list)
# result = [dict(**{'word': word}) for code in code_list]
# chi_root_list = [get_chi_root_list(code) for code in code_list]

# print(chi_root_list)
