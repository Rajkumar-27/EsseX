class Config(object):
   LOGGER = True
   API_ID = 1645928
   API_HASH = "6874b8b3d4aef43cd79cc32d0fc86af8"
   TOKEN = "1405317749:AAFejGg60ACk2qbH7bDTwTNuySAXgy5_jhU"
   DB_URI = "postgres://mrbcrvit:m3juoeaXEgJMOeUXhLqikEQaIA1vmfpb@satao.db.elephantsql.com:5432/mrbcrvit"

class Development(Config):
   TEST_DEVELOP = True
   LOGGER = True
