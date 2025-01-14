# Copyright (C) @nkka404
# Channel: https://t.me/premium_channel_404
import os
import time
import random
import requests

from telebot import TeleBot, types
from check import checker
from reg import reg
from hit_sender import send  
#from gen import gg
#from sk import check_sk

from config import BOT_TOKEN, ADMIN_ID
# Load the bot token
#with open('token.txt', 'r') as token_file:
    #token = token_file.read().strip()

bot = TeleBot(BOT_TOKEN, parse_mode="HTML")
subscriber = ADMIN_ID
allowed_users = [ADMIN_ID]  #Your ID

@bot.message_handler(commands=["start"])
def start(message):
	if str(message.chat.id) not in allowed_users:
		first_name = message.from_user.first_name
		username = message.from_user.username or " "
		user_id = message.from_user.id
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/nkka404")
		keyboard.add(contact_button)
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/bkddgfsa/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f"<strong><b>𝑯𝑬𝑳𝑳𝑶..</b> {first_name}\n"
        f"💥<b>Your Information:</b> 🎉\n\n"
        f"🔸<b>User ID:</b> <code>{user_id}</code>\n"
        f"🔸<b>User Name:</b> @{username}\n"
        f"🔸<b>User Subscribe => </b><code>Free☑️</code></strong>",parse_mode='html',reply_markup=keyboard)
		return	
	first_name = message.from_user.first_name
	username = message.from_user.username or " "
	user_id = message.from_user.id
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/premium_channel_404")
	keyboard.add(contact_button)
	random_number = random.randint(33, 82)
	photo_url = f'https://t.me/bkddgfsa/{random_number}'
	bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f"<strong><b>𝑯𝑬𝑳𝑳𝑶..</b> {first_name}\n"
        f"💥<b>Your Information:</b> 🎉\n\n"
        f"🔸<b>User ID:</b> <code>{user_id}</code>\n"
        f"🔸<b>User Name:</b> @{username}\n"
        f"🔸<b>User Subscribe => </b><code>Premium☑️</code></strong>",reply_markup=keyboard)
#End ☑️💥	
success_keys = ["Thank", "redirectUrl"]
insufficient_keys = ["Your card has insufficient funds."]
otp_keys = ["Verifying", "requires_action"]
cvv_keys = ["Your card does not support this type of purchase"]
incorrect_keys = [
    "security code is incorrect.", "your card's security code is incorrect",
    "security code is invalid."
]
failure_keys = ["your card has been declined", "Your card was declined."]
# Start the bot 🤖
@bot.message_handler(commands=['help'])
def run(message):
	key = types.InlineKeyboardMarkup()
	b1=types.InlineKeyboardButton(text='🔛 User Commands 🔛', callback_data='user')
	b2=types.InlineKeyboardButton(text='🔛 Owner Commands 🔛', callback_data='admin')
	b3=types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/nkka404")
	key.row_width = 1
	key.add(b1,b2,b3)
	#random_number = random.randint(33, 82)
	#photo_url = f'https://t.me/bkddgfsa/{random_number}'
	#first_name = message.from_user.first_name
	username = message.from_user.username or " "
	user_id = message.from_user.id
	##first_name = message.from_user.first_name or " "
    ##last_name = message.from_user.last_name or " "
	bot.send_message(message.chat.id,text=f"<strong><b>Online => ✅\nBot: @checkerbot404bot ♻️</b>\n"
        f"💥<b>Your Information:</b> 🎉\n\n"
        f"🔸<b>User ID:</b> <code>{user_id}</code>\n"
        f"🔸<b>User Name:</b> @{username}</strong>",parse_mode='html',reply_markup=key)
		#return 🚫
#bot.send_message(message.chat.id,text=f"<strong><b>Hello..</b> {first_name}! My name is 404 Checker CC.\n"
        #f"💥<b>Your Information:</b> 🎉\n\n"
        #f"🔸<b>User ID:</b> <code>{user_id}</code>\n"
        #f"🔸<b>User Name:</b> @{username}\n"
        #f"🔸<b>User Subscribe => </b><code>Premium☑️</code></strong>",parse_mode='html',reply_markup=key)
        #User Subscribe => [</b><code>Premium</code><b>]</b>"</strong>",parse_mode='html',reply_markup=key)

#@bot.message_handler(func= lambda m: True)

 
@bot.callback_query_handler(func=lambda call: True)
def qery(call):
	if call.data == 'user':
	  user(call.message)
	if call.data == 'admin':
	  admin(call.message)

@bot.message_handler(commands=["add"])
def add_user(message):
    if str(message.chat.id) == ADMIN_ID:  # Only bot owner can add new users
        try:
            new_user_id = message.text.split()[1]  # Extract new user ID from the command
            allowed_users.append(new_user_id)
            bot.reply_to(message, f"User ID {new_user_id} Has Been Added Successfully.✅\nCongratulations! Premium New User🎉✅ ")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /add 123456789")
    else:
        bot.reply_to(message, "You do not have permission to add users.🚫")
@bot.message_handler(commands=["delete"])
def delete_user(message):
    if str(message.chat.id) == subscriber:  # Only bot owner can delete users
        try:
            user_id_to_delete = message.text.split()[1]  # Extract user ID from the command
            if user_id_to_delete in allowed_users:
                allowed_users.remove(user_id_to_delete)
                bot.reply_to(message, f"User ID {user_id_to_delete} has been removed successfully.✅")
            else:
                bot.reply_to(message, "User ID not found in the list.🚫")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /delete 123456789")
    else:
        bot.reply_to(message, "You do not have permission to delete users.🚫")
    
import random
import string

# List to store generated redeem codes
valid_redeem_codes = []

# Function to generate a random redeem code in the format XXXX-XXXX-XXXX
def generate_redeem_code():
    code = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3))
    return code

# /code command handler to generate a new redeem code with a designed output
@bot.message_handler(commands=["code"])
def generate_code(message):
    if str(message.chat.id) == ADMIN_ID:  # Only the bot owner can generate codes
        new_code = generate_redeem_code()  # Generate a new code
        valid_redeem_codes.append(new_code)  # Store the generated code
        # Send the redeem code in a designed format
        bot.reply_to(
            message, 
            f"<b>🎉 New Redeem Code 🎉</b>\n\n"
            f"<code>{new_code}</code>\n\n"
            f"Use this code to redeem your access!", 
            parse_mode="HTML"
        )
    else:
        bot.reply_to(message, "You do not have permission to generate redeem codes.🚫")

# /redeem command handler (as explained earlier)
@bot.message_handler(commands=["redeem"])
def redeem_code(message):
    try:
        redeem_code = message.text.split()[1]  # Extract redeem code from message
    except IndexError:
        bot.reply_to(message, "Please provide a valid redeem code. Example: /redeem XXXX-XXXX-XXXX")
        return

    if redeem_code in valid_redeem_codes:
        if str(message.chat.id) not in allowed_users:
            allowed_users.append(str(message.chat.id))  # Add user to allowed list
            valid_redeem_codes.remove(redeem_code)  # Remove used code
            bot.reply_to(message, f"Redeem code {redeem_code} has been successfully redeemed.✅ You now have access to the bot.")
        else:
            bot.reply_to(message, "You already have access to the bot.")
    else:
        bot.reply_to(message, "Invalid redeem code. Please check and try again.")

@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in allowed_users:
		bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @nkka404")
		return
# Start the bot 🤖
#@bot.message_handler(func= lambda m: True)

# Start the bot
@bot.message_handler(commands=["user"])
def user(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @nkka404")
        return
    bot.reply_to(message,
    f"<b>🎉 User Commands:</b>\n\n"
            f"<b>Format: [command] XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>\n"
	    f"<b>Example: </b><code>/chk 4647331155846215|11|2024|630</code>\n\n"
            f"<b>Format: [command] XXXX-XXXX-XXXX</b>\n"
            f"<b>Example: </b><code>/redeem</code> <b>ABC1-ABC2-ABC3</b>\n\n"
            f"<b>💥User Subscribe => [</b><code>Premium</code><b>]</b>\n\n"
            f"𝐁𝐨𝐭 𝐁𝐲 -> @nkka404", 
            parse_mode="HTML"
        )
# Start the bot
@bot.message_handler(commands=["admin"])
def admin(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @nkka404")
        return
    bot.reply_to(
            message, 
            f"<b>🎉 Owner Commands:</b>\n\n"
            f"<b>- Add User => </b><code>/add [id]</code>\n\n"
            f"<b>- Remove User => </b><code>/delete [id]</code>\n\n"
            f"<b>- Generate Code => </b><code>/code</code>\n\n"
            f"<b>💥User Subscribe => [</b><code>Premium</code><b>]</b>\n\n"
            f"𝐁𝐨𝐭 𝐁𝐲 -> @nkka404", 
            parse_mode="HTML"
        )
# Start the bot
@bot.message_handler(commands=['chk'])
def check_card(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @nkka404")
        return
    try:
        cc = message.text.split('/chk', 1)[1].strip()
        user_id = message.from_user.id
        username = message.from_user.username or " "
        FIRST = message.from_user.first_name or " "
        LAST = message.from_user.last_name or " "

        msg = bot.reply_to(message, "<strong>Checking your card...</strong>")
        msg_id = msg.message_id  
        start_time = time.time()

        # Validate card format
        cc = reg(cc)
        if not cc:
            bot.edit_message_text(
                chat_id=message.chat.id, message_id=msg_id,
                text="Invalid card format. Please use the correct format: `cc|mm|yy|cvv`",
                parse_mode="Markdown"
            )
            return

        result2 = checker(cc)

        if any(k in result2 for k in success_keys):
            key = "Charged Card! £0.3🔥"
        elif any(k in result2 for k in insufficient_keys):
            key = "Insufficient Funds☑"
        elif any(k in result2 for k in otp_keys):
            key = "Declined Card 3DS☑"
        elif any(k in result2 for k in cvv_keys):
            key = "Declined Card CVV☑"
        elif any(k in result2 for k in incorrect_keys):
            key = "Declined Card CCN☑"
        elif any(k in result2 for k in failure_keys):
            key = "Your Card Declined❌"
        else:
            key = f"Unknown Response: {result2}"

        time_taken = round(time.time() - start_time, 2)

        send_response = send(cc, key, user_id, username, FIRST, LAST, time_taken)

        print(send_response)

        
        try:
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=msg_id,
                text=send_response,
                parse_mode="HTML" 
            )
        except Exception as e:
            print(f"Error editing message: {e}")
            print(f"Problematic Response: {send_response}")
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=msg_id,
                text="<strong>An error occurred while processing your request. Please try again later.</strong>"
            )

    except Exception as e:
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg_id,
            text="<strong>An error occurred while processing your request.</strong>"
        )
        print(f"Error: {e}")
        
# Start the 🤖
print("BOT RUNNING......")
bot.infinity_polling(timeout=25, long_polling_timeout=5)
#bot.run()


