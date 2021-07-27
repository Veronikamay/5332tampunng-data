# (c) Abangtamvan

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL"))
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
**𝕀ℕ𝔽𝕆 𝔹𝕆𝕋**
bot ini ᵐᵉʳᵘᵖᵃᵏᵃⁿ ˡᵃʸᵃⁿᵃⁿ ᵖᵉⁿʸⁱᵐᵖᵃⁿᵃⁿ ᵃʷᵃⁿ ᵗᵉˡᵉᵍʳᵃᵐ ᵈⁱᵐᵃⁿᵃ ᵏᵃᵐᵘ ᵇⁱˢᵃ ᵐᵉⁿʸⁱᵐᵖᵃⁿ ᵈᵃᵗᵃ ᵐᵃᵘᵖᵘⁿ ᶠⁱˡᵉ (ᵛⁱᵈᵉᵒ, ᵃᵘᵈⁱᵒ, ᵈᵒᵏᵘᵐᵉⁿ, ᵍᵃᵐᵇᵃʳ, ᵈˡˡ) ᵗᵃⁿᵖᵃ ʰᵃʳᵘˢ ᵗᵃᵏᵘᵗ ᵏᵉʰⁱˡᵃⁿᵍᵃⁿ ᶠⁱˡᵉ ᵗᵉʳˢᵉᵇᵘᵗ. ᵈⁱˢᵃᵐᵖⁱⁿᵍ ⁱᵗᵘ, ᵏᵃᵐᵘ ʲᵘᵍᵃ ᵇⁱˢᵃ ᵐᵉⁿᵍᵃᵏˢᵉˢ ᶠⁱˡᵉⁿʸᵃ ˢᵉʷᵃᵏᵗᵘ-ʷᵃᵏᵗᵘ ᵇⁱˡᵃ ᵈⁱᵖᵉˡᵘᵏᵃⁿ ᵈᵉⁿᵍᵃⁿ ᶜᵃʳᵃ ᵐᵉᵐᵇᵘᵏᵃ ᶠⁱˡᵉ ᵐᵉˡᵃˡᵘⁱ ˡⁱⁿᵏ ˡᵃˡᵘ ᵐᵉⁿᵈᵒʷⁿˡᵒᵃᵈⁿʸᵃ.\n\n**Link akan tersedia bila kamu telah subscribe channels dan telah mengirim data/file** !!


࿇ **ADMIN:** [K4N3N](https://t.me/K4N3N)

࿇ **SUPPORT CHANNEL** [GUDANGSYAHWAT76](https://t.me/gudangsyahwat76)

"""
	ABOUT_DEV_TEXT = f"""


**NOPE**
   ║█║▌║█║▌│║▌║▌█║


"""
	HOME_TEXT = """
**BOT CLOUD STORAGE** 🔥\n\n
Halo Kak : [{}](tg://user?id={}) Terimakasih udah Langganan Channel dan Menggunakan Bot ini.\n\n

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
🄽🄶🄴🅆🄴
🄳🅄🄻🅄
🄽🄶🄰🄿🄰
"""
