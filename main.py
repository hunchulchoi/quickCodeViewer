"""
    encoding=utf8
    author: 최훈철
    
    MIT License

    Copyright (c) 2022 최훈철

    맞춤형복지 코드 검색을 위한 플러그인 
    EDICT를 참고하여 만들었다.
    라이센스는 없으니까 마음대로 고쳐 쓰시면 된다.

"""

from encodings import utf_8
from json import load
from msilib.schema import Error
import re
from wox import Wox, WoxAPI


class QuickCode(Wox):
    """Easy Dictionay Class used by Wox"""

    def query(self, key):
        """Overides Wox query function to capture user input"""
        with open('CMN_CD.json', 'r', encoding='utf-8') as data_file:
            self.code = load(data_file)
        
        results = []

        # self.log_file =  open('test.txt', 'w', encoding='utf-8')

        try:
            self.search(key, results)
        except KeyError:
            try:
                pass
            except KeyError:
                pass

        # self.log_file.write(f'==================>results:{results}\n')
        # self.log_file.close()

        return results


    def search(self, pstr, results):

        # self.log_file.write(f'code:{len(self.code)}:{self.code[3]}\n')
        # self.log_file.write(f'pstr:{pstr}\n')

        if not pstr:
            pass
        else:

            p = re.compile(f'{pstr}')

            #self.log_file.write(f'p:{p}\n')

            for cd in self.code:
                # self.log_file.write(f'{(p.match(cd["CSF_CD_NM"]) or p.match(cd["CMN_CD_NM"]))}, cd[CSF_CD_NM]:{cd["CSF_CD_NM"]}, cd[CMN_CD_NM]:{cd["CMN_CD_NM"]}\n')
                if p.match(cd['CSF_CD_NM']) or p.match(cd['CMN_CD_NM']):
                    # self.log_file.write(f'if cd:{cd}\n')
                    result = {"Title": f"{cd['CSF_CD_NM']}({cd['CMN_CSF_CD']})", "SubTitle": f"{cd['CMN_CD']} - {cd['CMN_CD_NM']}", "IcoPath": "Images\\dog_robot.ico"}
                    # self.log_file.write(f'result:{result}\n')
                    results.append(result)
                        
            # self.log_file.write(f'results:{results}\n')

if __name__ == "__main__":
    QuickCode()