import time
from google_trans_new import google_translator
import re



class Translate(object):
    def __init__(self):
        # 初始化翻译文本路径以及翻译目标语言
        self.txt_file = 'd://code/index.html'
        self.aim_language = 'en'

        # 读入要翻译的文本文件

    def read_txt(self):
        with open(self.txt_file, 'r', encoding='utf-8')as f:
            txt = f.read()
        return txt

        # 进行文本处理，此为优化

    def cut_text(self, text):
        # 如果只是一行，就切割成5000字一次来翻译
        if len(text) == 1:
            str_text = ''.join(text).strip()
            # 筛选是一行但是文本长度大于5000
            if len(str_text) > 5000:
                # 使用正则表达式切割超长文本为5000一段的短文本
                result = re.findall('.{5000}', str_text)
                return result
            else:
                # 如果文本为一行但是这一行文本长度小于5000，则直接返回text
                return text
            """
            如果不止一行，加以判断
             (1)每行字符数都小于5000
            （2）有的行字符数小于5000，有的行字符数大于5000
            """
        else:
            result = []
            for line in text:
                # 第（1）种情况
                if len(line) < 5000:
                    result.append(line)
                else:
                    # 第（2）种情况，切割以后，追加到列表中
                    cut_str = re.findall('.{5000}', line)
                    result.extend(cut_str)
            return result

    def translate(self, text):
        if text:
            aim_lang = self.aim_language
            try:
                t = google_translator(timeout=10)
                translate_text = t.translate(text, aim_lang)
                print(translate_text)
                return translate_text
            except Exception as e:
                print(e)
