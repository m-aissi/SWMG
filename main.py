def translate(words):
    words = words.split(" ")
    translate = []
    for word in words:
        cuneiform = '𒋻𒁀𐏓𒁓𒀼𐎣𒋝𒀂𒐕𒑟𒐞𒁇𐎠𒐖𒆸𒇬𒌒𒇲𒑣𒈦𒑚𐎏𒉼𒉽𒌨𒑣'
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        translate.append(''.join([cuneiform[alphabet.index(c)] for c in word.lower()]))
    return " ".join(translate)

def cuneiform_translation(words):
    words = words.split(" ")
    translate = []
    for word in words:
        cuneiform = '𒋻𒁀𐏓𒁓𒀼𐎣𒋝𒀂𒐕𒑟𒐞𒁇𐎠𒐖𒆸𒇬𒌒𒇲𒑣𒈦𒑚𐎏𒉼𒉽𒌨𒑣'
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        translate.append(''.join([alphabet[cuneiform.index(c)] for c in word.lower()]))
    return " ".join(translate)


def custom_spell():
    custom_spell = input('Enter custom spell: ')
    print(translate(custom_spell))

def shadow_spell():
    shadow_spell_type = input('Select shadow spell type: \n 1. Curse of Mending \n 2. Curse of Mending \n')
    shadow_spell_type_map = [
        "Maledictum vinculi aeterni Ludio loricam tollere iam non potest",
        "Maledicta ablatione Perimit item cum ludio ludius moritur"
    ]
    print(translate(shadow_spell_type_map[int(shadow_spell_type) - 1]))

def fire_spell():
    fire_spell = 'Incendia incendia incendia incendia incendia'
    print(translate(fire_spell))

def frost_spell():
    frost_spell = 'Obscurum Aeternum In abysso superbi peccato primario gloriamur'
    print(translate(frost_spell))

def rollback():
    custom = input("Enter what you're trying to translate: ")
    print(cuneiform_translation(custom))

def get_user_input():
    while True:
        cuneiform_input = input('Select spell type : \n 1. Custom \n 2. Shadow Spell \n 3. Fire Spell \n 4. Frost Spell \n 5. Rollback\n\n Choice> ')
        if cuneiform_input not in ['1', '2', '3', '4', '5']:
            print('Invalid input') 
        return cuneiform_input

def splash_screen():
    splash = """                                                                      
                                                                      
  ,----..               ,-.----.    .--.--.       ,---,.    ,---,     
 /   /   \         ,--, \    /  \  /  /    '.   ,'  .' |  .'  .' `\   
|   :     :      ,'_ /| ;   :    \|  :  /`. / ,---.'   |,---.'     \  
.   |  ;. / .--. |  | : |   | .\ :;  |  |--`  |   |   .'|   |  .`\  | 
.   ; /--`,'_ /| :  . | .   : |: ||  :  ;_    :   :  |-,:   : |  '  | 
;   | ;   |  ' | |  . . |   |  \ : \  \    `. :   |  ;/||   ' '  ;  : 
|   : |   |  | ' |  | | |   : .  /  `----.   \|   :   .''   | ;  .  | 
.   | '___:  | | :  ' ; ;   | |  \  __ \  \  ||   |  |-,|   | :  |  ' 
'   ; : .'|  ; ' |  | ' |   | ;\  \/  /`--'  /'   :  ;/|'   : | /  ;  
'   | '/  :  | : ;  ; | :   ' | \.'--'.     / |   |    \|   | '` ,/   
|   :    /'  :  `--'   \:   : :-'   `--'---'  |   :   .';   :  .'     
 \   \ .' :  ,      .-./|   |.'               |   | ,'  |   ,.'       
  `---`    `--`----'    `---'                 `----'    '---'         
                                                                      """
    print(splash)

if __name__ == "__main__":
    splash_screen()
    cuneiform = '𒋻𒁀𐏓𒁓𒀼𐎣𒋝𒀂𒐕𒑟𒐞𒁇𐎠𒐖𒆸𒇬𒌒𒇲𒑣𒈦𒑚𐎏𒉼𒉽𒌨𒑣 '
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    cuneiform_to_alphabet = dict(zip(alphabet, cuneiform)) # {'𒋻': 'a', '𒁀': 'b', '𐏓': 'c',..}

    cuneiform_input = get_user_input() 

    # Define spell, Add new spell by adding
    cuneiform_map = [
        custom_spell,
        shadow_spell,
        fire_spell,
        frost_spell,
        rollback
    ]

    try:
        print(cuneiform_input)
        cuneiform_map[int(cuneiform_input) - 1]()
    except Exception as e:
        print(e)
        print("Unknow spell")