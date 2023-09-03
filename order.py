import requests
import pandas as pd
import time
import random
from tqdm import tqdm
import datetime

cookies = {
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
