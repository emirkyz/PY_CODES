#with open("my_file.txt") as file:
#    contents = file.read()     ## with kullanarak open ve close yapmak gereksinimi kalkar
#    print(contents)            ## otomatik open close yapar bu
    
with open("my_file.txt", mode = "a") as file: # "w" olursa içindekileri siler
    file.write("\nNew text")                    # "a" olunca en sona ekler


with open("new_file.txt", mode = "w") as file:  # verilen isimde dosya yoksa oluşturur
    file.write("\nNew text")