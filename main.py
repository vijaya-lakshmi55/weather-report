import os  # modules
import file
import graph

count = 1
end = "yes"
print('Weather Forecasting⛈️🌤️🌦️🌈🌞')
while end != "no":  # while loop is used for iterating

    file.ppt_file()
    end = input("Do you want to search for other location: ").lower()  # taking input from user.
    if end in ['yes','y']:
        count += 1
        continue
    else:
        filename = input("Enter your file name: ")  # taking input from user.
        if count > 1:  # if count >1 it will represent the graph.
            graph.graph()
        file.prs.save(f'{filename}.pptx')
        os.system(f'{filename}.pptx')
