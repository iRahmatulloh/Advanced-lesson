import argparse
import requests
import json


parser = argparse.ArgumentParser(description='Bu dastur Quron surasi va oyati raqamini kiritishingiz kerak\nshunda '
                                             'oyat matnini qaytaradi', epilog='Dasturni ishlatganingiz uchun rahmat!')
parser.add_argument('surah', type=int, help='Suraning raqamini kiriting!')
parser.add_argument('ayah', type=int, help='Suraning oyat raqamini kiritishingiz kerak!\nE`tiborli bo`ling!!')
args = parser.parse_args()


ask_ayah = requests.get(f"http://api.alquran.cloud/v1/ayah/{args.surah}:{args.ayah}/en.asad")
res = ask_ayah.json()
print(json.dumps(res['data']['text']))
