cuneiform = '𒋻𒁀𐏓𒁓𒀼𐎣𒋝𒀂𒐕𒑟𒐞𒁇𐎠𒐖𒆸𒇬𒌒𒇲𒑣𒈦𒑚𐎏𒉼𒉽𒌨𒑣 '
alphabet = 'abcdefghijklmnopqrstuvwxyz '
cuneiform_to_alphabet = dict(zip(alphabet, cuneiform)) # {'𒋻': 'a', '𒁀': 'b', '𐏓': 'c',..}

# on va request l'user input EN LEGENDE
print("ntm")
cuneiform_input = input('Select spell type : \n 1. Custom \n 2. Shadow Spell \n 3. Fire Spell \n 4. Frost Spell \n ')
# fail safe pour les inputs
while cuneiform_input not in ['1', '2', '3', '4']:
    print('Invalid input') 
    cuneiform_input = input('Select spell type : \n 1. Custom \n 2. Shadow Spell \n 3. Fire Spell \n 4. Frost Spell \n')
    

# on fait un switch

if cuneiform_input == '1':
        custom_spell = input('Enter custom spell: \n').lower()
        for each in custom_spell:
            print(cuneiform_to_alphabet[each], end='')
            
if cuneiform_input == '2':
    shadow_spell_type = input('Select shadow spell type: \n 1. Curse of Mending \n 2. Curse of Vanishing \n')
    if(shadow_spell_type == '1'):
        shadow_spell = "Maledictum vinculi aeterni Ludio loricam tollere iam non potest".lower()
        spell_tab = shadow_spell.split()
        spell_translation = []
        for word in spell_tab:
            for char in word:
                spell_translation.append(cuneiform_to_alphabet[char])
            # spell_translation.append(' ')
        print(''.join(spell_translation))
    elif(shadow_spell_type == '2'):
        curse_mending = 'MaledictaablationePerimititemcumludioludiusmoritur'.lower()
        for char in curse_mending:
            print(cuneiform_to_alphabet[char], end='')
if cuneiform_input == '3':
    fire_spell = 'Incendia incendia incendia incendia incendia'.lower()
    for char in fire_spell:
        print(cuneiform_to_alphabet[char], end='')
if cuneiform_input == '4':
    frost_spell = 'ObscurumAeternumInabyssosuperbipeccatoprimariogloriamur'.lower()
    for char in frost_spell:
        print(cuneiform_to_alphabet[char], end='')
    