import requests
import pandas as pd
import time
import random
from tqdm import tqdm
import datetime

cookies = {
'REC_T_ID':'f3304d85-43c9-11ed-a22b-b47af14b5674', 
'SPC_F':'8svj7SInezqJadZboDBcHT2uA9znUBJR', 
'_hjSessionUser_868286':'eyJpZCI6IjIzMzBhNWNlLWE3ZDQtNTUxYS1iYzBlLWQxYmQzNWE4OWQ2YSIsImNyZWF0ZWQiOjE2NjQ4NzcwMjEzNTQsImV4aXN0aW5nIjp0cnVlfQ==', 
'SC_DFP':'eSmynoZSVafdoFbHSwnChdDsmsNPgzfi', 
'_fbp':'fb.1.1678150441980.1401009225', 
'_gcl_au':'1.1.332219217.1686153963', 
'_gcl_aw':'GCL.1688226763.Cj0KCQjwnf-kBhCnARIsAFlg492VF7DZo-1HApWXwLwwtkeZ0aFvXV_TVmBtMesBnI36lRtNFfrsS1AaAlGqEALw_wcB', 
'_gac_UA-61914164-6':'1.1688226766.Cj0KCQjwnf-kBhCnARIsAFlg492VF7DZo-1HApWXwLwwtkeZ0aFvXV_TVmBtMesBnI36lRtNFfrsS1AaAlGqEALw_wcB', 
'_med':'refer', 
'_ga_3XVGTY3603':'GS1.1.1691091385.1.1.1691091446.60.0.0',
'SPC_CLIENTID':'OHN2ajdTSW5lenFKokfwvlvkryhvluxn', 
'SPC_SC_TK':'2c2c10aa5078691233a6755bf043e554', 
'SPC_SC_UD':'543086523', 
'SPC_STK':'ROqGt9YWHhogcf8PrD6kxod3ypMCyXdubk2GHg5ktSAIVxuUny1bMsGXhFh64V0vXpFEzMwB8HNfruH97HIhE9CmvcQ1tECruWc0m09BgWTAWLu9XGmAIgS9iD2HLNW4degOiiKzKl5Il1HSvd7EOmWGMkeud9vvoC6cVeApm1w=', 
'SPC_SI':'Bb7IZAAAAAAxQjJuMGtIbqB7aQAAAAAAM0Y5WTQ2ek8=', 
'_gid':'GA1.2.775980971.1691593417', 
'csrftoken':'9LZLqzTGR72CP2b8u34lQMsEKORvGGRQ', 
'_QPWSDCXHZQA':'c0374b62-bea3-4e81-cf70-73ab28acb028', 
'AMP_TOKEN':'%24NOT_FOUND', 
'SPC_ST':'.R1FTbnVzM0h0SklkSHhtaFlHSdaBzJj1MWAhN5cUZpc5wE2p/1ws/RKfiu7eOKse9mc956WmThjVgMRn7tEXtF9v0b6Q+mVttLhQn5kjU14V+YxcF/zWgwdnDOkhI0hxzTAtKRq/NOpNxShitWYRVM/SIQKOIwzIOvKlnramRY+51Aact/1AToznFDmzNJwEeB773jBwzxUbBBbjXfBH1Q==', 
'SPC_U':'88681865', 
'SPC_R_T_ID':'hn0CPTDf4+HhQMCoHGO1t3irDdTGKY654w4vSqTPyuIFv74z75lyO00890ZZsfJfmNzE3tELikHN4LN7uQXztqDmQ06humy0coCQWjUq7Qv8Xcwu99B6K+70ocdj66isfyk2gdb2X32bkixEoB9qOG2opMZ+jrV+VcLmgYKM79w=', 
'SPC_R_T_IV':'bGVHT095YVBLemEyTlI2ZQ==', 
'SPC_T_ID':'hn0CPTDf4+HhQMCoHGO1t3irDdTGKY654w4vSqTPyuIFv74z75lyO00890ZZsfJfmNzE3tELikHN4LN7uQXztqDmQ06humy0coCQWjUq7Qv8Xcwu99B6K+70ocdj66isfyk2gdb2X32bkixEoB9qOG2opMZ+jrV+VcLmgYKM79w=', 
'SPC_T_IV':'bGVHT095YVBLemEyTlI2ZQ==', 
'shopee_webUnique_ccd':'B0jEessh2veGYu4lRJwzaw%3D%3D%7CERg3SXCzXZp15PrZcN0sNujchORMxm4QO8yHVEzo0OHkZVoiJVSnAyx1BYpPLY3v4T63RST0cx4%3D%7CUgzbiFvPGv%2B27054%7C08%7C3', 
'ds':'aa7da06106acc1d8a4151a755a924eb1', 
'_ga':'GA1.1.462356251.1678150443', 
'_ga_M32T05RVZT':'GS1.1.1691635269.28.1.1691635473.60.0.0', 
'SPC_EC':'SlNDSFA5bnR4SzhTbjliWfaaFgMlMc6tT6BNjBVRA9vuJYU/coGGXNV9aXT8URwxcTQp66iRaVor6O/L3k2m6TbmX/R1R7P3B4nDYU8oslaOFX6CIfPIsMhW+VNVBaOw8Tje3aEvQGv+RCkFjv7o5u4PFgIzlmPQbql4CRwNVt0=',
}

headers = {
    'Referer':'https://shopee.vn/user/purchase/',
    'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':"Windows",
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Api-Source':'pc',
    'X-Csrftoken':'9LZLqzTGR72CP2b8u34lQMsEKORvGGRQ',
    'X-Requested-With':'XMLHttpRequest',
    'X-Shopee-Language':'vi',
    'X-Sz-Sdk-Version':'unknown',
}

params = {
    'limit': 5,
    'offset': 0,
}


order = []


for i in tqdm(range(0, 301, 5)):
    params['offset'] = i
    response = requests.get('https://shopee.vn/api/v4/order/get_all_order_and_checkout_list', headers=headers, params=params, cookies=cookies)
    if response.status_code == 200:
        data = response.json().get('data').get('order_data').get('details_list')
        if data is not None:
            for j in range(len(data)):
                    order_info = data[j]
                    main = order_info.get('info_card').get('order_list_cards')[0].get('product_info').get('item_groups')[0].get('items')[0]
                    main1 = order_info.get('info_card').get('order_list_cards')[0].get('shop_info')
                    main2 = order_info.get('shipping', {}).get('tracking_info', {})
                    product_id = main.get('item_id')
                    shop_id = main1.get('shop_id')
                    name = main.get('name')
                    price = main.get('item_price') / 100000 
                    amount = main.get('amount')
                    shop_name = main1.get('shop_name')
                    status = main2.get('description', 'Đã hủy')
                    if status == 'Đã hủy':
                        status = None  
                        time = None    
                    else:
                        time = datetime.datetime.fromtimestamp(main2.get('ctime', 0))
                
                    order.append({
                        'Mã sản phẩm': product_id,
                        'Mã shop': shop_id,
                        'Tên sản phẩm': name,
                        'Giá': price,
                        'Số lượng': amount,
                        'Tên shop': shop_name,
                        'Trạng thái đơn hàng': status,
                        'Giao hàng vào lúc': time
                    })
        
            
df = pd.DataFrame(order)
df.to_csv('order_details.csv', index=False, encoding='utf-8-sig')
