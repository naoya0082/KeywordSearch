# 使えそうだったので講義内のコードをコピー

import urllib3

http = urllib3.PoolManager()
r = http.request('GET',
                 'https://ads.google.com/aw/keywordplanner/home?ocid=297764154&__c=2416736746&sourceid=awo&__u=5731789613&authuser=0')
r.status

# class AddressSearcher:
#     def __init__(self):
#         self.base_url = f"http://zipcloud.ibsnet.co.jp/api/search"
#
#     def search(self, postal_code):
#         url = f"{self.base_url}?zipcode={postal_code}"
#         response = requests.get(url)
#         response_dict = response.json()
#
#         if response_dict["results"] is None:
#             return "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"
#
#         return self.location(response_dict)
