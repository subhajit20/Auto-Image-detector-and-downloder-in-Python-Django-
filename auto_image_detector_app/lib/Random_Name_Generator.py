import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
integernumbers = [1,2,3,4,5,6,7,8,9]
# characters = ['!','@','#','$','%','^','&','*','_','[',']','~']


def Random_Name_Generetor(length):
    newname = 'IMG'
    if length > 9:
        return 0
    else:
        for i in range(0,length):
            random_number = int(random.random() * length)
            phase_one = str(alphabets[random_number])
            phase_two = str(integernumbers[random_number])
            # phase_three = str(characters[random_number])
            newname += f'{phase_one}{phase_two}{phase_two}{phase_one}'

        
        return f'{newname}.jpg'