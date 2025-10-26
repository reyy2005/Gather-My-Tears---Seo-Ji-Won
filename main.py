import sys
import time
import os 

def play_music() : 
    
    lyrics = [
        ('오, 그대여', 0.12),                    
        ('난 기다릴 거예요', 0.10),              
        ('내 눈물의 편지 하늘에 닿으면', 0.09),   
        ('오-오-오-오', 0.15),                   
        ('언젠가 그대 돌아오겠죠 내게로', 0.09),  
        ('(아, 아, 아) 오, 오-오', 0.13),        
        ('난 믿을 거예요', 0.11),                 
        ('눈물 모아', 0.13)                      
    ]
    delays = [
        1.9, 2.2, 2.5, 4.2, 1.8, 3.8, 1.7, 3.0   
    ]
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' + '='*50)
    print('🎵  Gather My Tears - Seo Ji Won  🎵'.center(50))
    print('='*50 + '\n')
    time.sleep(2.5) 
    
    for i, (char_line, char_delay) in enumerate(lyrics):
        for char in char_line:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(char_delay)
            
        time.sleep(delays[i])
        print('')
        
play_music()