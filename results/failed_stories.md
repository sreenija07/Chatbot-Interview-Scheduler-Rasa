## happy path 1 (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_close_chat -->


## happy path 2 (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_close_chat -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_close_chat -->


## sad path 1 (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: option1: not good -->
    - utter_cheer_up   <!-- predicted: utter_close_chat -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_close_chat -->


## sad path 2 (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: option1: not good -->
    - utter_cheer_up   <!-- predicted: utter_close_chat -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_close_chat -->


## sad path 3 (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: mood_great: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_close_chat -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_close_chat -->


## say goodbye (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_close_chat -->


## bot challenge (C:\Users\hi\AppData\Local\Temp\tmpm3jn85re\73751254d72a47068ffdc6769dc4bdf0_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: goodbye: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_close_chat -->


