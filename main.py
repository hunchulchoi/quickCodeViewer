"""
    encoding=utf8
    author: ashutosh
    
    MIT License

    Copyright (c) 2020 Ashutosh

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    Notes:
        -The dictionary_compact_with_words.json file used in this project is modified form of
            dictionary_compact.json file sourced from https://github.com/matthewreagan/WebstersEnglishDictionary
            that in turn depends upon Project Gutenberg's Webster's Unabridged English Dictionary
            https://www.gutenberg.org/ebooks/29765.
        -The spell.py file used in this project is sourced from  Peter Norvig's website norvig.com
           http://norvig.com/spell-correct.html. The file is modified for the current use case.
"""

from encodings import utf_8
from json import load
import re
from wox import Wox, WoxAPI


class QuickCode(Wox):
    """Easy Dictionay Class used by Wox"""

    def _add_result(self, definitions, results, max_results):
        """Adds first two definitions to the result sent to Wox"""
        for definition in definitions.split(';')[:max_results]:
            if definition[0].isdigit():
                definition = definition[3:]
            try:
                definition = definition[:definition.index('.')]
            except ValueError:
                pass
            try:
                definition.strip()[0].upper()+definition.strip()[1:]
            except IndexError:
                pass
            result = {"Title": definition, 'SubTitle': None,
                      "IcoPath": "Images\\dog_robot.ico"}
            if correction_flag:
                result['SubTitle'] = f'Showing results for "{key}" (auto-corrected)'
            else:
                result['SubTitle'] = f'Showing results for "{key}"'
            results.append(result)

    def query(self, key):
        """Overides Wox query function to capture user input"""
        with open('code.json', 'r', encoding='utf-8') as data_file:
            self.code = load(data_file)
        #words = self.edict['cb2b20da-9168-4e8e-8e8f-9b54e7d4444']
        #spell_correct = SpellCorrect(words)
        results = []
        try:
            self.search(key, results, 4)
            #self._add_result(definitions, results, key, 4)
        except KeyError:
            try:
                #corrected_key = key #spell_correct.correction(key)
                #definitions = self.edict[corrected_key]
                #self._add_result(definitions, results, corrected_key, 4)
                pass
            except KeyError:
                pass

        if not results:
            pass

        return results


    def search(self, pstr, results, max_result):

        log_file =  open('text.txt', 'w', encoding='utf-8')

        log_file.write(f'code:{self.code}\n')

        print(f'=====:{pstr}')
        log_file.write(f'pstr:{pstr}\n')

        if not pstr:
            pass
        else:

            p = re.compile(f'[{pstr}]+')

            print(f'p:{p}')
            log_file.write(f'p:{p}\n')

            for cd in self.code:
                log_file.write(f'cd:{cd}\n')
                log_file.write(f"p.match({cd['column']}):{p.match(cd['column'])}\n")
                if p.match(cd['column']) or p.match(cd['name']):
                    #result = {"Title": f"{cd['column']}({cd['name']})", 'SubTitle': f"{cd['code']} {cd['cd']}", "IcoPath": "Images\\dog_robot.ico"}
                    result = {"Title": f"{cd['column']}", "SubTitle": f"{cd['code']}", "IcoPath": "Images\\dog_robot.ico"}
                    results.append(result)

            log_file.write(f'results:{results}\n')
            log_file.close()


if __name__ == "__main__":
    QuickCode()
