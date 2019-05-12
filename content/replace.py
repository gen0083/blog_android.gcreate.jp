import os
import re

make_directry_which_has_images = False
stack = []


def collect_md_files(file):
    if os.path.isdir(file):
        file_list = os.scandir(file)
        for file in file_list:
            collect_md_files(file)
    else:
        base, ext = os.path.splitext(file)
        print("base:", base, " ext:", ext)
        if ext == ".md":
            stack.append(file)


def replace_tags(src):
    open_p = re.compile(r'<p>')
    close_p = re.compile(r'</p>')
    tag_header = re.compile(r'<h(\d).*>(.+?)</h\d>')
    tag_break = re.compile(r'<br.*>')
    rename_cover_image = re.compile(r'cover_image:')
    open_pre_code = re.compile(r'<pre><code>')
    close_pre_code = re.compile(r'</code></pre>')
    inline_code = re.compile(r'<code>(.+?)</code>')
    alert_block = re.compile(r'<div id="wppda_alert">.+?</div>')
    lt_code = re.compile(r'&lt;')
    gt_code = re.compile(r'&gt;')
    amp_code = re.compile(r'&amp;')
    quote_code = re.compile(r'&quot;')
    single_quote_code = re.compile(r'&#039;')

    def convert_header(m):
        count = int(m.group(1))
        content = m.group(2)
        return "\n" + "#" * count + " " + content + "\n\n"

    def convert_inline_code_block(m):
        body = m.group(1)
        return "`" + body + "`"

    def replace_source(source):
        dst = open_p.sub("", source)
        dst = close_p.sub("\n", dst)
        dst = tag_header.sub(convert_header, dst)
        dst = tag_break.sub("", dst)
        dst = rename_cover_image.sub("featuredimage:", dst)
        dst = open_pre_code.sub("\n```\n", dst)
        dst = close_pre_code.sub("```\n", dst)
        dst = inline_code.sub(convert_inline_code_block, dst)
        dst = alert_block.sub("", dst)
        dst = lt_code.sub("<", dst)
        dst = gt_code.sub(">", dst)
        dst = quote_code.sub('"', dst)
        dst = single_quote_code.sub("'", dst)
        dst = amp_code.sub("&", dst)
        return dst

    return replace_source(src)


# collect target files
base_path = os.path.dirname(__file__)
file_list = os.scandir(os.path.join(base_path, "post"))
for file in file_list:
    collect_md_files(file)

# work on each file
print("stack size: ", len(stack))
image_tag = re.compile(r'<img src="https://android\.gcreate\.jp/')
for file in stack:
    file_path = os.path.abspath(file)
    print("stack: ", file_path)
    with open(file_path, mode="r+") as f:
        src = f.read()
        # do replace here
        after = replace_tags(src)
        # end replace
        f.close()
        if make_directry_which_has_images:
            has_image = image_tag.search(src)
            if has_image:
                dir_name, ext = os.path.splitext(file_path)
                os.mkdir(dir_name)
    with open(file_path, mode="w") as f:
        f.write(after)
        f.close()
