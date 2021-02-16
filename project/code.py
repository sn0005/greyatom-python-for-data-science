# --------------
#Code starts here

#Function to read file
def read_file(path):
    file = open(path,'r')
    #Opening of the file located in the path in 'read' mode
    
    #Reading of the first line of the file and storing it in a variable
    sentence = file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
read_file(file_path)
#Printing the line of the file
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)    
print(message_1)
print(message_2)

#Function to fuse message
def fuse_msg(message_a,message_b):
    quotient= int(message_b)//int(message_a)
    return quotient
secret_msg_1 = str(fuse_msg(message_1,message_2))

message_3 = read_file(file_path_3)
print(message_3)
#Function to substitute the message
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    #If-else to compare the contents of the file
    return sub
secret_msg_2 = substitute_msg(message_3)
    
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)
    

def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list = message_d.split(" ")
    
    #Splitting the message into a list
    b_list = message_e.split(" ")
    
    #Comparing the elements from both the lists
    c_list = []
    for i in a_list:
        if not i in b_list:
            c_list.append(i)
    
    #Combining the words of a list back to a single string sentence
    final_msg = " ".join(c_list)
    
    #Returning the sentence
    return final_msg
    

#Calling the function to read file
secret_msg_3 = compare_msg(message_4, message_5)

#Calling the function to read file
message_6 = read_file(file_path_6)
print(message_6)

#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list = message_f.split(" ")
    
    #Creating the lambda function to identify even length words
    even_word = lambda x : len(x)%2 == 0
    
    #Splitting the message into a list
    b_list = list(filter(even_word, a_list))
    
    #Combining the words of a list back to a single string sentence
    final_msg = " ".join(b_list)    
    
    #Returning the sentence
    return final_msg
    
#Calling the function to read file
secret_msg_4 = extract_msg(message_6)

message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = " ".join(message_parts)

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Function to write inside a file
def write_file(secret_msg,path):
       
    #Opening a file named 'secret_message' in 'write' mode
    a = open(path,'a+')

    #Writing to the file
    a.write(secret_msg)

    #Closing the file
    a.close()

#Calling the function to write inside the file    
write_file(secret_msg,final_path)
print(secret_msg)

#Printing the entire secret message


#Code ends here


