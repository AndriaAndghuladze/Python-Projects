import random #შემთხვევითი ელემენტების ასარჩევად.
import array # გამოიყენება სიმბოლოების მასივის შესაქმნელად და შერევისთვის


MAX_LEN = 10 #მაქსიმალური რიცხვები ან ასოები


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #ციფრები რაც შეიძლება იქნას გამოყენებული პაროლში

LOWER_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z'] #პატარა ასოები რაც შეიძლება იქნას გამოყენებული პაროლშიც 

UPPER_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']#დიდი ასოები რაც შეიძლება იქნას გამოყენებული პაროლში

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']#სიმბლოლოები რაც შეიძლება იქნას გამოყენებული პაროლში


COMBINED_LIST = DIGITS + UPPER_CHARACTERS + LOWER_CHARACTERS + SYMBOLS #სიები გაერთიან


rand_digit = random.choice(DIGITS) #ერთი ციფრი
rand_upper = random.choice(UPPER_CHARACTERS) #ერთი დიდი ასო
rand_lower = random.choice(LOWER_CHARACTERS) #ერთი პატარა ასო
rand_symbol = random.choice(SYMBOLS) #ერთი სიმბოლო


temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol #ვაწყობთ პაროლს


for x in range(MAX_LEN - 4): #გიდე 6 რიცხვი, ასო ან სიმბოლოა საჭირო
    temp_pass = temp_pass + random.choice(COMBINED_LIST) #ირჩევა COMBINED_LIST-იდან და შესაძლებელია რომ ყველანაირი სიმბოლო იყოს გამოყენებული

#თავიდან მიღებული პაროლი შეიძლება ყოველთვის იწყებოდეს ციფრით, შემდეგ დიდი ასოთი და ა.შ.ამიტომ ვურევთ ერთმანეთში რომ შემთხვევით ადგილებზე დადგნენ
temp_pass_list = array.array('u', temp_pass)
random.shuffle(temp_pass_list)

#შერეული მასივის ელემენტები აერთდება უკან სტრიქონად, რომელიც არის საბოლოო პაროლი.
password = ""
for x in temp_pass_list:
    password = password + x

#ვაკონსოლებთ ჩვენს კოდს
print(password)


password = ""
for x in temp_pass_list:
    password = password + x

print('*' *len(password))