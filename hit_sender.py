import requests

def send(cc, key, user_id, username, FIRST, LAST, time_taken):
    ii = cc[:6]

    try:
        response = requests.get(f'https://binchk-api.vercel.app/bin={ii}')
        #response = requests.get(f'https://bins.antipublic.cc/bins/'+{ii})
        data = response.json()

        if data.get('status', False):
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            country_name = data.get('country', 'Unknown')
            country_flag = data.get('flag', '🏳️')
            bank = data.get('bank', 'Unknown')
            #New-Method
        else:
            bank = country_flag = country_name = status = brand = card_type = 'Unknown'
    except Exception as e:
        print(f"Error fetching data from binchk API: {e}")
        bank = country_flag = country_name = status = brand = card_type = 'Unknown'

    msg1 = f"""
<b> ✦ API Stripe Charged [ £0.30 ] </b>
<b>≫────≪Card Info≫────≪</b>
<b>[ϟ] Cc: </b><code>{cc}</code>
<b>[ϟ] Response: {key}</b>

<b>[ϟ] Bin:</b> <code>{ii}</code>
<b>[ϟ] Info:</b> <code>{card_type} - {brand}</code>
<b>[ϟ] Bank:</b> <code>{bank}</code>
<b>[ϟ] Country:</b> <code>{country_name} [{country_flag}]</code>

<b>[ϟ] T/t:</b> <code>{time_taken}(Seconds)</code> | [<b>St:</b> <code>True</code>] 
<b>≫────≪User Info≫────≪</b>
<b>[ϟ] Req by:</b> <a href="tg://user?id={user_id}">{FIRST} {LAST}</a></strong>
"""

    return msg1
