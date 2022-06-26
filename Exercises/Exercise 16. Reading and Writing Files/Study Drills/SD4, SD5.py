# we use 'w' to open the file in write mode. When we do that, everything will be deleted.
# So we don't need to truncate the file unless when we want to
# open the file in read mode and truncating the text at the same time.