post_likes = eval(input("put your input is here: "))

total_likes = 0

for post in post_likes:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes += 0
print(total_likes)

# [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
