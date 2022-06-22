import glob
import os
import re

format_white_list = [".txt", ".tex", ".sty"]

# get files
files = glob.glob("./*")
for file in files:
    format: str = os.path.splitext(file)[1]
    if format in format_white_list:
        # read files
        with open(file) as reader:
            content = reader.read()

        # check
        print(file)

        # replace!
        # env command
        content = content.replace("{Prf}", "{prf}")
        content = content.replace("{Def}", "{dfn}")
        content = content.replace("{Thm}", "{thm}")
        content = content.replace("{Lem}", "{lem}")
        content = content.replace("{Pro}", "{prp}")
        content = content.replace("{Cor}", "{cor}")
        content = content.replace("{Rem}", "{rem}")
        content = content.replace("{Ex}", "{ex}")
        # math inline command
        content = re.sub("\$([^\$]+)\$", r"\( \1 \)", content)
        # write and save
        dirname, filename = os.path.split(file)
        with open(dirname + "out_" + filename, "w") as writer:
            writer.write(content)
