import os
import string

def get_text():
    print('1. direct text entry\n2. file path input')
    choice = input('select choice (1 or 2): ').strip()
    
    if choice == "1":
        lines = []
        while True:
            line = input()
            if line.strip() == "$$END_TEXT$$":
                break
            lines.append(line)
        return '\n'.join(lines)
        
    elif choice == "2":
        while True:
            path = input('enter file path : ').strip()
            if os.path.exists(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception:
                    pass
            print('invalid path - try again.')
    return ""

def preprocess_text(raw_text):
    clean_text = raw_text.lower().translate(str.maketrans('', '', string.punctuation))
    word_list = clean_text.split()
    chars_only = "".join(word_list)
    return word_list, chars_only

def display_dashboard(word_list, chars_only):
    total_words = len(word_list)
    unique_words = len(set(word_list))
    total_chars = len(chars_only)
    
    char_freq = {}
    for char in chars_only:
        char_freq[char] = char_freq.get(char, 0) + 1
        
    print("\n================ DASHBOARD ================")
    print(f'total word count        :{total_words}')
    print(f'unique word count       :{unique_words}')
    print(f'total chars (no spaces) :{total_chars}')
    print('character frequencies :')
    for char, count in sorted(char_freq.items()):
        print(f"  '{char}': {count}")
    print("===========================================")

def main():
    raw_text = get_text()
    if not raw_text.strip():
        print('no text provided.')
        return
        
    word_list, chars_only = preprocess_text(raw_text)
    
    while True:
        print("\n--- main menu ---")
        print("1. consolidated text analytics dashboard")
        print("2. exit")
        
        option = input('choose an option : ').strip()
        if option == '1':
            display_dashboard(word_list, chars_only)
        elif option == '2':
            break
        else:
            print('invalid option.')

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
    
    